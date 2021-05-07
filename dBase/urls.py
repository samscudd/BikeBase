from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),

	path('bikes/<int:bike_id>/', views.bike, name='bike'),

	path('wheels/<int:wheel_id>/', views.wheel, name='wheel'),

	path('wheelsets/', views.wheel_sets, name='wheelsets'),

	path('frontwheels/', views.front_wheels, name='frontwheels'),

	path('rearwheels/', views.back_wheels, name='rearwheels'),

	path('bikes/<int:bike_id>/wheels/<int:wheel_id>/', views.bike_wheelset, name='complete1'),

	path('wheelsets/<int:wheel_id>/', views.wheel, name='wheelset_complete'),

	path('bikes/<int:bike_id>/<str:type>/<int:wheel_id>/', views.bike_wheel, name='halfway'),

	path('bikes/<int:bike_id>/<str:type1>/<int:wheel1_id>/<str:type2>/<int:wheel2_id>/', views.completion, name='complete2')

]
