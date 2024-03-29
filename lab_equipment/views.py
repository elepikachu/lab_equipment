import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET
from rent.models import Item, Suggestion
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opt


VERSION = '装备所仪器设备共享平台'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    if request.method == 'GET':
        all_data = Item.objects.all()
        class_box = ['全部']
        city_box = []
        cnt = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        for item in all_data:
            if item.classic not in class_box:
                class_box.append(item.classic)
            if item.city not in city_box:
                city_box.append(item.city)
        cnt['a'] = all_data.count()
        cnt['b'] = all_data.filter(status__exact='正常，运转').count()
        cnt['c'] = all_data.filter(status__exact='正常，待机').count()
        cnt['d'] = all_data.filter(status__exact='停机，待维修').count()
        cnt['e'] = all_data.filter(city__exact='北京').count()
        cnt['f'] = all_data.filter(city__exact='廊坊').count()
        bar1 = Bar(init_opts=opt.InitOpts(theme=ThemeType.MACARONS))
        bar1.add_xaxis(['共计', '在用', '待机', '在修'])
        bar1.add_yaxis('设备数', [cnt['a'], cnt['b'], cnt['c'], cnt['d']])
        bar1.set_global_opts(title_opts=opt.TitleOpts(title='设备使用情况统计图'))
        chart_option1 = bar1.dump_options_with_quotes()
        bar2 = Bar(init_opts=opt.InitOpts(theme=ThemeType.PURPLE_PASSION))
        bar2.add_xaxis(['共计', '北京', '廊坊'])
        bar2.add_yaxis('设备数', [cnt['a'], cnt['e'], cnt['f']])
        bar2.set_global_opts(title_opts=opt.TitleOpts(title='设备区域统计图'))
        chart_option2 = bar2.dump_options_with_quotes()
        dic = {'ver': VERSION, 'class': class_box, 'city': city_box, 'cnt': cnt, 'crt': chart_option1,
               'ctr': chart_option2}
        return render(request, 'main.html', dic)
    elif request.method == 'POST':
        if 'search' in request.POST:
            word = request.POST['word']
            return HttpResponseRedirect(
                'equipment?word=%s' % (word))
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
# 函数名： info_view
# 功能： 网站说明
# -------------------------------------------------------------
def question_view(request):
    dic = {'ver': VERSION}
    return render(request, 'question.html', dic)


# -------------------------------------------------------------
# 函数名： get_ip
# 功能： 获取电脑主机ip
# -------------------------------------------------------------
def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# -------------------------------------------------------------
# 函数名： contact_view
# 功能： 联系我们
# -------------------------------------------------------------
def contact_view(request):
    if request.method == 'GET':
        dic = {'ver': VERSION}
        return render(request, 'contact.html', dic)
    if request.method == 'POST':
        if 'sub' in request.POST:
            sug = request.POST['sug']
            typ = request.POST['typ']
            if Suggestion.objects.exists():
                idx = Suggestion.objects.latest('id').id
            else:
                idx = 0
            Suggestion.objects.create(id=idx + 1, ip=get_ip(request), date=datetime.datetime.today(), detail=sug,
                                      type=typ, finish=0)
            return HttpResponseRedirect('/')


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
