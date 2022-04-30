from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('profile.html', views.profile, name="profile"),
	path('medical_card.html', views.medicalcard, name="medicalcard"),
	path('schedule.html', views.schedule, name='schedule'),
	path('patient_sch.html', views.patientsch, name="patientsch"),
	path('app.html', views.app, name="app")
]
