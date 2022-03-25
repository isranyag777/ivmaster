from django.db import models

class Operator(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=3)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    ipaddress = models.CharField(max_length=12)

    def __str__(self):
        return self.username


class Action(models.Model):
    oprtid = models.CharField(max_length=3)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    action = models.CharField(max_length=50)

    def __str__(self):
        return self.action




