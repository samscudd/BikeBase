from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.views.generic.edit import CreateView

from .models import Bikes, Wheels


def index(request):
	bike_list = Bikes.objects.all()
	wheel_list = Wheels.objects.all()
	front_wheels = Wheels.objects.filter(front=True)
	rear_wheels = Wheels.objects.filter(back=True)
	wheelsets = Wheels.objects.filter(front=True, back=True)
	context = {
		'bike_list': bike_list,
		'wheel_list': wheel_list,
		'front': front_wheels,
		'back': rear_wheels,
		'wheelsets' : wheelsets
	}
	return render(request, 'dBase/index.html', context)

def bike(request, bike_id):
	bike = Bikes.objects.get(id=bike_id)
	compatible_wheelsets = Wheels.objects.filter(size=bike.wheel_size, brakes=bike.brakes_mounts, front=True, back=True)
	compatible_front = Wheels.objects.filter(size=bike.wheel_size, brakes=bike.brakes_mounts, front=True)
	compatible_back = Wheels.objects.filter(size=bike.wheel_size, brakes=bike.brakes_mounts, back=True)
	context = {
		'bike' : bike,
		'wheelsets': compatible_wheelsets,
		'front' : compatible_front,
		'back' : compatible_back
	}
	return render(request, 'dBase/bike.html', context)
	

def wheel(request, wheel_id):
	wheel = Wheels.objects.get(id=wheel_id)
	wheelModel = wheel.wheel_model
	compatible_bikes = Bikes.objects.filter(wheel_size=wheel.size, brakes_mounts=wheel.brakes)
	context = {
		'wheelset' : wheel,
		'bikes' : compatible_bikes
	}
	return render(request, 'dBase/wheels.html', context)

def wheel_sets(request):
	wheels = Wheels.objects.filter(front=True, back=True)
	context = {
		'wheels' : wheels
	}
	return render(request, 'dBase/bike.html', context)

def front_wheels(request):
	wheels = Wheels.objects.filter(front=True)
	context = {
		'type' : 'front',
		'wheels' : wheels
	}
	return render(request, 'dBase/bike.html', context)

def back_wheels(request):
	wheels = Wheels.objects.filter(back=True)
	context = {
		'type' : 'rear',
		'wheels' : wheels
	}
	return render(request, 'dBase/bike.html', context)


def bike_wheel(request, bike_id, type, wheel_id):
	bike = Bikes.objects.get(id=bike_id)
	wheel = Wheels.objects.get(id=wheel_id)
	if(type =="front"):
		compatible_wheels = Wheels.objects.filter(size=bike.wheel_size, brakes=bike.brakes_mounts, back=True)
		context = {
		'frontwheel' : wheel,
		'bike' : bike,
		'back' : compatible_wheels
		}
	else:
		compatible_wheels = Wheels.objects.filter(size=bike.wheel_size, brakes=bike.brakes_mounts, front=True)
		context = {
		'backwheel' : wheel,
		'bike' : bike,
		'front' : compatible_wheels
		}
	return render(request, 'dBase/bike.html', context)

def completion(request, bike_id, type1, wheel1_id, type2, wheel2_id):
	bike = Bikes.objects.get(id=bike_id)
	if(type1 == "front"):
		frontwheel = Wheels.objects.get(id=wheel1_id)
		backwheel = Wheels.objects.get(id=wheel2_id)
	else:
		frontwheel = Wheels.objects.get(id=wheel2_id)
		backwheel = Wheels.objects.get(id=wheel1_id)	
	context = {
		'frontwheel' : frontwheel,
		'backwheel' : backwheel,
		'bike' : bike
	}
	return render(request, 'dBase/finished.html', context)

def secondWheel(request, type, wheel_id):
	wheel = Wheels.objects.get(id=wheel_id)
	if(type =="front"):
		compatible_wheels = Wheels.objects.filter(size=wheel.size, brakes=wheel.brakes, back=True)
		context = {
		'wheel' : wheel,
		'bike' : bike,
		'back' : compatible_wheels
		}
	else:
		compatible_wheels = Wheels.objects.filter(size=wheel.size, brakes=wheel.brakes, front=True)
		context = {
		'wheel' : wheel,
		'bike' : bike,
		'front' : compatible_wheels
		}
	return render(request, 'dBase/bike.html', context)

def finalBike(request, type1, wheel1_id, type2, wheel2_id):
	wheel = Wheels.objects.get(id=wheel1_id)
	compatible_bikes = Bikes.objects.filter(wheel_size=wheel.size, brakes_mounts=wheel.brakes)
	if(type1 == "front"):
		frontwheel = Wheels.objects.get(id=wheel1_id)
		backwheel = Wheels.objects.get(id=wheel2_id)
	else:
		frontwheel = Wheels.objects.get(id=wheel2_id)
		backwheel = Wheels.objects.get(id=wheel1_id)	
	context = {
		'frontwheel' : frontwheel,
		'backwheel' : backwheel,
		'bikes' : compatible_bikes
	}
	return render(request, 'dBase/wheels.html', context)
# Create your views here.