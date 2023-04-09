from django.urls import path
from api import views

urlpatterns = [ 
    path('', views.getOverView),
    path('sellers/', views.getAllSeller),
    path('createSeller/', views.createSeller),
    path('clients/', views.getAllClient),
    path('createClient/', views.createClient)
]
