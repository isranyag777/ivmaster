from django.http import Http404
from django.shortcuts import render, redirect
from .models import Usuario, Sucursal
import numpy as np
import pymysql
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

# VISTAS BASADAS EN FUNCIONES

#Necesito definir una vista home para obtener en primera instancia una sucursal
@login_required
def home(request):
    sucursales = Sucursal.objects.all()

    return render(request, 'home.html', {'sucursales':sucursales})



def connection():
    connection = pymysql.connect(user='root', passwd='L1nuxf0r3v3r.', db='xtream_iptvpro', host=host, port=port)
    cur = connection.cursor()

    return cur, connection


#PRUEBA DE EXISTENCIA DE NUEVA RAMA


@login_required
def listusers(request, name):
    user = request.user.username

    sucursales = Sucursal.objects.all()
    for suc in sucursales:
        if suc.name == name:                    #Verificar si el dato que se pasa de la vista anterior existe en la lista de sucursales
            if user in suc.operators:           #Veificar si el usuario tiene acceso a esa sucursal
                global host
                global scname
                global port
                host = suc.ipaddress
                scname = suc.name
                port = suc.port
            else:
                return redirect('/')

    #Se retorna una lista de objetos
    #usuarios = Usuario.objects.all()
    usuarios = getuserasobj()           #En teoría se emuló la función de consulta de arriba (ORM). Esto con la finalidad de obtener la data directamente de la DB de Xtrm y no de la DB de la pagina web
    queryset = request.GET.get("search")
    if queryset:
        usuarios = getuniqueuserobj(queryset)

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(usuarios, 5)
        usuarios = paginator.page(page)
    except:
        raise Http404

    return render(request, 'gestionUsuarios.html', {'usuarios': usuarios, 'paginator':paginator, 'sucursales': sucursales, 'sucselected': name})


@login_required
def newuser(request):
    #Necesito enviar al hmtl lista de usuarios y matriz de planes

    bouquets= getbouquets()

    return render(request, 'newUser.html', {'dtbouquets': bouquets})



@login_required
def createuser(request):

    name = request.POST['txtUsername']
    password = request.POST['txtPassword']
    maxconn = request.POST['txtConn']
    #plan = request.POST['slcplan[]']

    plan = request.POST.getlist('slcplan[]')
    plan = str(plan)
    plan = ''.join(x for x in plan if x not in "' ")


    #Verificación de existencia de un usuario:

    cur, conn = connection()
    comando0 = "SELECT username FROM users WHERE username = '" + name + "';"
    cur.execute(comando0)
    rows = cur.fetchall()
    rows = np.array(rows)

    if rows.size == 0:
        cur, conn = connection()
        comando = "INSERT INTO users (username, password, bouquet, max_connections," \
                  "allowed_ips, allowed_ua, created_at, created_by) VALUES ('"+name+"','"+\
                  password+"','"+plan+"','"+maxconn+"','[]','[]','01010101','1');"
        cur.execute(comando)

        comando2 = "SELECT id FROM users WHERE username = '"+ name +"';"
        cur.execute(comando2)
        rows = cur.fetchall()
        rows = np.array(rows)
        idvar = rows[0][0]
        idvar = str(idvar)

        comando3 = "INSERT INTO user_output (user_id, access_output_id) VALUES ('" + idvar + "', '1');"
        cur.execute(comando3)
        comando3 = "INSERT INTO user_output (user_id, access_output_id) VALUES ('" + idvar + "', '2');"
        cur.execute(comando3)
        comando3 = "INSERT INTO user_output (user_id, access_output_id) VALUES ('" + idvar + "', '3');"
        cur.execute(comando3)

        conn.commit()
        conn.close()

        return redirect('/users/'+scname)

    else:
        messages.warning(request, '¡Username ya existe!')
        return redirect('/users/'+scname)


@login_required
def edituser(request, username):
    usuariounico = getuserunique(username)
    bouquets= getbouquets()

    return render(request, 'editUser.html', {'usr':usuariounico, 'freebqts':bouquets})

@login_required
def updateuser(request, username):
    password = request.POST['txtPassword']
    maxconn = request.POST['txtConn']
    plan = request.POST.getlist('slcplan[]')
    plan = str(plan)
    plan = ''.join(x for x in plan if x not in "' ")

    cur, conn = connection()
    comando = "UPDATE users SET password = '" +password+ "', bouquet = '"+ plan +"', max_connections = "+maxconn+" WHERE username = '"+ username +"';"

    cur.execute(comando)
    conn.commit()
    conn.close()

    messages.success(request, username + ': ¡Usuario actualizado!')


    return redirect('/users/'+scname)



@login_required
def deleteuser(request, username):
    cur, conn = connection()
    comando = "DELETE FROM users WHERE username = '" + username + "';"
    cur.execute(comando)
    conn.commit()
    conn.close()

    messages.success(request, username + ': ¡Usuario eliminado!')

    return redirect('/users/'+scname)

@login_required
def disableuser(request, username):
    cur, conn = connection()
    comando = 'UPDATE users SET enabled = 0 WHERE (username = "' + username + '");'
    cur.execute(comando)
    conn.commit()
    conn.close()

    return redirect('/users/'+scname)

@login_required
def enableuser(request, username):
    cur, conn = connection()
    comando = 'UPDATE users SET enabled = 1 WHERE (username = "' + username + '");'
    cur.execute(comando)
    conn.commit()
    conn.close()

    return redirect('/users/'+scname)

@login_required
def banuser(request, username):
    cur, conn = connection()
    comando = 'UPDATE users SET admin_enabled = 0 WHERE (username = "' + username + '");'
    cur.execute(comando)
    conn.commit()
    conn.close()

    return redirect('/users/'+scname)

@login_required
def unbanuser(request, username):
    cur, conn = connection()
    comando = 'UPDATE users SET admin_enabled = 1 WHERE (username = "' + username + '");'
    cur.execute(comando)
    conn.commit()
    conn.close()

    return redirect('/users/'+scname)



# FUNCIONES PARA OBTENER LA DATA DE XTRM .. Esto tiene que emular el ORM de Django, es decir poder hacer consultas
# y obtener el resultado en forma de lista de objetos

#Se define la clase User(Esta no conecta a ningun modelo de la DB, es una clase independiente)
class User:
    def __init__(self, usr,pwd,mcn,bqt,stt):
        self.username = usr
        self.password = pwd
        self.maxconn = mcn
        self.bouquet = bqt
        self.status = stt

    def __str__(self):
        return self.username


#Mejor trabajemos con funciones
def getuserasobj():
    # Obtiene todos los datos, correspondientes a SQL: SELECT * FROM Usuario
    cur, conn = connection()
    comando = "SELECT username, password, max_connections, bouquet, admin_enabled, enabled FROM users;"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)           #Esto genera una lista de Strings por cada usuario
    conn.commit()
    conn.close()
    # Para seguir con la estructura de Django, necesito retornar usuarios como una lista de objetos
    listobj = []
    for row in rows:
        listobj.append(User(row[0], row[1], row[2], getbqtname(row[3]), getstate(row[4], row[5])))

    return listobj


def getuniqueuserobj(queryset):
    # Obtiene todos los datos, correspondientes a SQL: SELECT * FROM Usuario
    cur, conn = connection()
    comando = "SELECT username, password, max_connections, bouquet, admin_enabled, enabled  FROM users WHERE (username LIKE '%"+ queryset + "%');"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)           #Esto genera una lista de Strings por cada usuario
    conn.commit()
    conn.close()
    # Para seguir con la estructura de Django, necesito retornar usuarios como una lista de objetos
    listobj = []
    for row in rows:
        listobj.append(User(row[0], row[1], row[2], getbqtname(row[3]), getstate(row[4], row[5])))

    return listobj


def getuserunique(usern):
    cur, conn = connection()
    comando = "SELECT username, password, max_connections, bouquet, admin_enabled, enabled  FROM users WHERE (username = '" + usern + "');"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)  # Esto genera una lista de Strings por cada usuario
    rows = rows[0]
    conn.commit()
    conn.close()
    # Para seguir con la estructura de Django, necesito retornar usuarios como una lista de objetos
    usuario = User(rows[0], rows[1], rows[2], getbqtname(rows[3]), getstate(rows[4], rows[5]))

    return usuario


def getstate(admin, enabled):
    status = 1
    #Tabla de verdad:
    if int(admin) == 1 & int(enabled) == 1:
        status = 0      #Activo
    else:
        if int(admin) == 0:
            status = 1      #Corte
        if int(enabled) == 0:
            status = 2      #Suspension       (Suspension debe predominar sobre el corte: Si esta cortado y suspendido, el estado es suspendido)

    return status
    # 0 activo
    # 1 cortado
    # 2 suspendido


def getbqtname(ids):
    ids = ''.join(x for x in ids if x not in "[]")
    ids = ids.split(',')

    cur, conn = connection()
    comando = "SELECT id, bouquet_name FROM bouquets;"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)  # Esto genera una lista de Strings por cada usuario
    conn.commit()
    conn.close()

    planname = ''
    for row in rows:
        for id in ids:
            if id == row[0]:
                planname = planname + ', ' + row[1]

    return planname[2:]


class Bouquet:
    def __init__(self, id,bqtname):
        self.id = id
        self.bqtname = bqtname


    def __str__(self):
        return self.bqtname



def getbouquets():
    cur, conn = connection()
    comando = "SELECT id, bouquet_name FROM bouquets;"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)

    conn.commit()
    conn.close()

    listobj = []
    for row in rows:
        listobj.append(Bouquet(row[0], row[1]))

    return listobj



def veruserexists(username):
    cur, conn = connection()
    comando = "SELECT username FROM users WHERE username = '"+username+"';"
    cur.execute(comando)
    rows = cur.fetchall()
    rows = np.array(rows)

    rows.size

    conn.commit()
    conn.close()