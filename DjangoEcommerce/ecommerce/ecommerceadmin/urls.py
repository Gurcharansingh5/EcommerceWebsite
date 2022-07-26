from django.urls import path
from . import views
urlpatterns = [

    path('',views.productdetails,name='productdetails'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('productdelete/<int:id>',views.productdelete,name='productdelete'),
    path('productupdate/<int:id>',views.productupdate,name='productupdate')

]