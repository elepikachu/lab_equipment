from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET
from rent.models import Item


VERSION = '装备所仪器设备共享平台'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    if request.method == 'GET':
        all_data = Item.objects.all()
        class_box = []
        city_box = []
        cnt = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        for item in all_data:
            if item.classic not in class_box:
                class_box.append(item.classic)
            if item.city not in city_box:
                city_box.append(item.city)
        class_box.append('全部')
        cnt['a'] = all_data.count()
        cnt['b'] = all_data.filter(status__exact='正常，运转').count()
        cnt['c'] = all_data.filter(status__exact='正常，待机').count()
        cnt['d'] = all_data.filter(status__exact='停机，待维修').count()
        dic = {'ver': VERSION, 'class': class_box, 'city': city_box, 'cnt': cnt}
        return render(request, 'main.html', dic)
    elif request.method == 'POST':
        if 'search' in request.POST:
            pass
        else:
            loc = request.POST['loc']
            classic = request.POST['type']
            return HttpResponseRedirect(
                'equipment?loc=%s&type=%s' % (loc, classic))


# -------------------------------------------------------------
# 函数名： info_view
# 功能： 网站说明
# -------------------------------------------------------------
def info_view(request):
    dic = {'ver': VERSION}
    return render(request, 'info.html', dic)


# -------------------------------------------------------------
# 函数名： robots_txt
# 功能： robots.txt
# -------------------------------------------------------------
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: *",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")