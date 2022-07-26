from django.shortcuts import render,HttpResponse,redirect
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/authlogin')
def adminindex(request):
    if request.method == 'POST':
        product_images = request.FILES['image']
        name = request.POST['name']
        price = request.POST['price']
        available = request.POST['darkmode']
        datasave = product(
            productname = name,
            productimage = product_images,
            productprice = price,
            status = available,
        )
        datasave.save()

        return HttpResponse(' data uploaded succesfly')
    else:
        return render(request,'adminindex.html')

def productdetails(request):
    productdata = product.objects.all()

    return render(request,'productdetails.html',{'productdata':productdata})

@login_required(login_url='authlogin')
def productdelete(request,id):
    if request.method == 'POST':
        blog_delete = product.objects.filter(id=id)
        blog_delete.delete()
        return redirect('productdetails')
    else:
        return render(request, 'delete.html', {'id': id})

@login_required(login_url='authlogin')
def productupdate(request,id):

    updateproduct = product.objects.get(id=id)
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        print(name)
        price = request.POST['price']
        print(price)
        updateproduct.productimage = image
        updateproduct.productname = name
        updateproduct.productprice = price
        updateproduct.save()
        return redirect('productdetails')
    else:
        return render(request, 'productupdate.html',{'updateproduct':updateproduct,'id':id})
