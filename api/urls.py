from django.urls import path
from api import views

urlpatterns = [ 
    path('', views.getOverView),
    path('sellers/', views.getAllSeller),
    path('createSeller/', views.createSeller),
    path('SellerById/<int:seller_id>/', views.SellerById.as_view()),

    path('clients/', views.getAllClient),
    path('createClient/', views.createClient),
    path('clientById/<int:client_id>/', views.ClientById.as_view()),

    path('admins/', views.adminList)
]
