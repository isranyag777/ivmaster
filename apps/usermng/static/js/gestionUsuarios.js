(function(){

    var statuscr = document.querySelectorAll(".cirstatus");
    var estados = [];
    var btcortar = document.querySelectorAll(".cortarjs");
    var btactivar = document.querySelectorAll(".activarjs");
    var btsuspender = document.querySelectorAll(".suspenderjs");
    var bthabilitar = document.querySelectorAll(".habilitarjs");
    var bteliminar = document.querySelectorAll(".eliminarjs");

    statuscr.forEach(st => {
        estados.push(st.dataset.status);
    });

    btcortar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea realizar la accion seleccionada?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });

    btactivar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea realizar la accion seleccionada?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });

    btsuspender.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea realizar la accion seleccionada?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });

    bthabilitar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea realizar la accion seleccionada?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });

    bteliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que desea eliminar el registro?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });


    var i;
    for (i=0;i <= estados.length; i++){
        
        var estado = estados[i]
        stt = statuscr[i];
        btncut = btcortar[i];
        btnact = btactivar[i];
        btnsusp = btsuspender[i];
        btnhab = bthabilitar[i];


        if (estado != '2'){
            btnhab.style.display = "none";

            if (estado === '0'){
                stt.style.backgroundColor = "green";
                btnact.style.display = "none";

            }
            if (estado === '1'){
                stt.style.backgroundColor = "#f0643b";
                btncut.style.display = "none";
            }            
        }
        else{
            stt.style.backgroundColor  = "gray";
            btnsusp.style.display = "none";
            btncut.style.display = "none";
            btnact.style.display = "none";

        }    
    }
})();

(function () {
    ('[data-toggle="tooltip"]').tooltip()
});
