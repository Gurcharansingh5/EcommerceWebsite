from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('authlogin',views.authlogin,name= 'authlogin'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('registers',views.register,name ='registers'),
    path('itemdetail/<int:id>',views.itemdetail,name='itemdetail'),
    path('purhcase/<int:id>',views.purchase,name='purchase'),
    path('orders',views.orders,name='orders'),
    path('rating/<int:id>',views.rating,name = 'rating'),
    path('payment',views.payment,name='payment')

]
