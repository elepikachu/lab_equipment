from django.shortcuts import render
from .models import Item
from lab_equipment.views import VERSION


def equipment_view(request):
    if request.method == 'GET':
        loc = request.GET['loc']
        lab = request.GET['lab']
        type = request.GET['type']
        data = Item.objects.filter(city__exact=loc, lab__exact=lab, classic__exact=type)
        ver = VERSION
        return render(request, 'equipment.html', locals())


def detail_view(request, item_id):
    item = Item.objects.get(id=item_id)
    dic = {'ver': VERSION, 'item': item, 'img': 'image/' + str(item.id) + '.jpg'}
    print(dic)
    return render(request, 'detail.html', dic)