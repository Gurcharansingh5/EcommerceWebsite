from django.contrib import admin
from . models import *
# Register your models here.

class products(admin.ModelAdmin):
    list_display = ('id','productimage','productname','productprice','status')
admin.site.register(product,products)

class sale(admin.ModelAdmin):
    list_display = ('id','name','phone','address','productid','userid','Date')
admin.site.register(buy,sale)

class rate(admin.ModelAdmin):
    list_display = ('id','products','givenby','stars','title','description')
admin.site.register(Rating,rate)