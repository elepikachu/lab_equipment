from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET
from rent.models import Item


VERSION = '装备所仪器设备展示共享平台 1.0.0'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    if request.method == 'GET':
        all_data = Item.objects.all()
        class_box = []
        for item in all_data:
            if item.classic not in class_box:
                class_box.append(item.classic)
        class_box.append('全部')
        dic = {'ver': VERSION, 'class': class_box}
        return render(request, 'main.html', dic)
    elif request.method == 'POST':
        loc = request.POST['loc']
        lab = request.POST['lab']
        classic = request.POST['type']
        return HttpResponseRedirect(
            '/equipment?loc=%s&lab=%s&type=%s' % (loc, lab, classic))


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