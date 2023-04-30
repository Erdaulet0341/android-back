from django.urls import path
from api import views

urlpatterns = [ 
    path('sellers/', views.Sellers.as_view()),
    path('createSeller/', views.Sellers.as_view()),
    path('SellerById/<int:seller_id>/', views.SellerById.as_view()),
    path('SellerById/<int:seller_id>/products/', views.getOneSellerProdcts),

    path('clients/', views.Clients.as_view()),
    path('createClient/', views.Clients.as_view()),
    path('clientById/<int:client_id>/', views.ClientById.as_view()),

    path('admins/', views.adminList),

    path('categories/<int:category_id>/products', views.getOneCategoryProdcts),
    path('categories/', views.Categoties.as_view()),
    path('categotyByName/<str:name>/', views.CategoryByName),
    path('categotyByID/<int:category_id>/', views.CategoryById.as_view()),


    path('products/', views.Products.as_view()),
    path('popularProducts/', views.popularProducts),
    path('productById/<int:product_id>/', views.ProductById.as_view()),


    path('ratings/', views.RatingsView.as_view()),
    path('ratings/<int:product_id>/', views.RatingById.as_view()),

    path('likes/', views.LikeProduct.as_view()),
    path('likes/<int:client_id>/', views.LikeProductById.as_view()),
    path('likesDel/<int:product_id>/', views.LikeProductById.as_view()),
]
