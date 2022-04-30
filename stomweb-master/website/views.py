from django.shortcuts import render
from .models import  prof_information  
from .models import medical_card
from .models import lt_service
from .models import id16200422
from .models import appointment

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	return render(request, 'contact.html', {})

def profile(request):
	prof_info = prof_information.objects.all()
	name_inp = 'Dana Ramazanova'
	return render(request, 'profile.html', {'prof_info': prof_info, 'name': name_inp})

def medicalcard(request):
	med_card = medical_card.objects.all()
	name_inp = 'Dana Ramazanova'
	return render(request, 'medical_card.html', {'med_card': med_card, 'name': name_inp})

def schedule(request):
	schedule = lt_service.objects.all()
	name_inp = 'Dana Ramazanova'
	return render(request, 'schedule.html', {'schedule': schedule, 'name': name_inp})

def patientsch(request):
	id = id16200422.objects.all
	return render(request, 'patient_sch.html', {'id16200422': id})

def app(request):
	app = appointment.objects.all
	name_inp = 'Dana Ramazanova'
	return render(request, 'app.html', {'app': app, 'name': name_inp})