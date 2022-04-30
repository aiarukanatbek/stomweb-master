import email
from django.db import models
from django.forms import CharField

# Create your models here.

class prof_information(models.Model):
    full_name = models.CharField(max_length=50)
    profile_img = models.ImageField()
    email = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

class lt_service(models.Model):
    id_num = models.IntegerField();
    service = models.CharField(max_length=20)
    patient = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)

class id16200422(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    cabinet = models.IntegerField()

class medical_card(models.Model):
    prof_img = models.ImageField()
    full_name = models.CharField(max_length=50)
    birth_dmy = models.DateField()
    birth_plc = models.CharField(max_length=50)
    cong_dis = models.CharField(max_length=100)
    blood_tp = models.CharField(max_length=3)

class appointment(models.Model):
    number = models.IntegerField()
    service = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    patient = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    cabinet = models.IntegerField()