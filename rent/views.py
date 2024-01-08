from django.db.models import Case, When, Value, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Item
from lab_equipment.views import VERSION


def equipment_view(request):
    if request.method == 'GET':
        all_data = Item.objects.all()
        class_box = ['全部']
        city_box = []
        # 仪器按照分类的展示顺序
        type_order = Case(
            When(classic__exact='电镜', then=Value(0)),
            When(classic__exact='3D打印设备', then=Value(1)),
            When(classic__exact='样品表征检测设备', then=Value(2)),
            When(classic__exact='样品处理设备', then=Value(3)),
            When(classic__exact='电化学测试设备', then=Value(4)),
            When(classic__exact='机械工艺测试设备', then=Value(5)),
            When(classic__exact='氢能-燃料电池测试设备', then=Value(6)),
        )
        for item in all_data:
            if item.classic not in class_box:
                class_box.append(item.classic)
            if item.city not in city_box:
                city_box.append(item.city)
        if 'loc' in request.GET:
            loc = request.GET['loc']
            classic = request.GET['type']
            if request.GET['type'] == '全部':
                data = Item.objects.filter(city__exact=loc).order_by(type_order)
            else:
                data = Item.objects.filter(city__exact=loc, classic__exact=classic)
        elif 'word' in request.GET:
            word = request.GET['word']
            classic = '关键词：' + word
            data = Item.objects.filter(Q(name__icontains=word) | Q(brand__icontains=word) | Q(num__icontains=word) |
                                       Q(classic__icontains=word)).order_by(type_order)
        else:
            data = all_data.order_by(type_order)
            classic = '全部'
        ver = VERSION
        return render(request, 'equipment.html', locals())
    if request.method == 'POST':
        if 'search' in request.POST:
            word = request.POST['word']
            return HttpResponseRedirect(
                'equipment?word=%s' % (word))


def detail_view(request, item_id):
    if request.method == 'GET':
        item = Item.objects.get(id=item_id)
        item.time = item.time.strftime('%Y年%m月%d日')
        classic = item.classic
        loc = item.city
        data = Item.objects.filter(classic__exact=classic, city__exact=loc)
        img = 'image/' + str(item.id)
        num = []
        for i in range(item.image):
            num.append(i+1)
        ver = VERSION
        return render(request, 'detail.html', locals())
    if request.method == 'POST':
        if 'booke' in request.POST:
            pass
        if 'print' in request.POST:
            pass

