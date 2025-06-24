
from django.urls import path
from. import views

urlpatterns = [
    path('', views.main, name='main'),

    #login
    path('login/', views.login_view, name='login'),
    path('login/signup', views.signup, name='signup'),

    #profile
    path('profile/<str:email>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    

    #product
    path('product/', views.product_view, name='product'),

    #Order
    path('product/order/<str:product_id>/', views.order, name='order'),
    path('product/order/<int:order_id>/review/', views.add_review, name='add_review'),
    path('product/orderhistory/', views.my_orders, name='my_orders'),
    path('product/delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
            path('product/update_order/<int:order_id>/', views.update_order, name='update_order'),

    #Review
    path('product/review/<str:product_id>/', views.review, name='review'),

    
]
