from django.urls import path

from travelapp import views

app_name = 'travel'
urlpatterns = [

    path('', views.demo, name='demo'),
    path('about/', views.about, name='about'),

]
