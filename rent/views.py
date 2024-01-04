from django.shortcuts import render
from .models import Item
from lab_equipment.views import VERSION


def equipment_view(request):
    if request.method == 'GET':
        all_data = Item.objects.all()
        class_box = ['全部']
        city_box = []
        for item in all_data:
            if item.classic not in class_box:
                class_box.append(item.classic)
            if item.city not in city_box:
                city_box.append(item.city)
        if 'loc' in request.GET:
            loc = request.GET['loc']
            type = request.GET['type']
            if request.GET['type'] == '全部':
                data = Item.objects.filter(city__exact=loc)
            else:
                data = Item.objects.filter(city__exact=loc, classic__exact=type)
        else:
            data = all_data.order_by('classic')
            type = '全部'
        ver = VERSION
        return render(request, 'equipment.html', locals())


def detail_view(request, item_id):
    item = Item.objects.get(id=item_id)
    type = item.classic
    loc = item.city
    data = Item.objects.filter(classic__exact=type, city__exact=loc)
    img = 'image/' + str(item.id) + '.jpg'
    ver = VERSION
    return render(request, 'detail.html', locals())