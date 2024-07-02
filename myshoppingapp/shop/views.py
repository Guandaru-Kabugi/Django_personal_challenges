from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Item
from django.template import loader
# Create your views here.

# def index (request):
#     item_list = Item.objects.all()
#     template = loader.get_template('shop/index.html')
#     context = {
#         'item_list': item_list,
#     }
#     return HttpResponse(template.render(context,request))
def index (request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'shop/index.html', context)
def shoes (request):
    return HttpResponse("This will be the shoes page!")
def clothes (request):
    return HttpResponse("This will be the clothes page!")
def detail (request, item_id):
    item = Item.objects.get(pk=item_id)
    context= {
        'item':item,
    }
    return render(request,'shop/detail.html',context)