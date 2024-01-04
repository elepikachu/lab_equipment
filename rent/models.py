from django.db import models


class Item(models.Model):
    id = models.IntegerField('编号', primary_key=True)
    name = models.CharField('设备名称', max_length=20, default='')
    classic = models.CharField('设备分类', max_length=20, default='其他设备')
    brand = models.CharField('仪器品牌', max_length=30, default='')
    time = models.DateTimeField('引进时间')
    num = models.CharField('仪器型号', max_length=50, default='')
    function = models.CharField('功能用途', max_length=300, default='')
    book = models.CharField('预约方式', max_length=10, default='线上')
    status = models.CharField('设备状态', max_length=20, default='')
    image = models.IntegerField('设备图片', default=0)
    research = models.CharField('支撑课题', max_length=20, default='')
    para = models.CharField('关键参数', max_length=500, default='')
    detail = models.CharField('关键配件', max_length=100, default='')
    city = models.CharField('城市', max_length=8, default='')
    locate = models.CharField('设备所在地', max_length=20, default='')
    lab = models.CharField('负责科室', max_length=20, default='')
    people = models.CharField('负责人', max_length=20, default='')
    contact = models.CharField('联系方式', max_length=60, default='')
    price = models.IntegerField('价格', default=0)


class Suggestion(models.Model):
    id = models.IntegerField('建议编号', primary_key=True)
    ip = models.CharField('操作ip', max_length=50, default='')
    date = models.DateTimeField('提出时间')
    type = models.CharField('建议类型', max_length=30, default='')
    detail = models.CharField('建议', max_length=500, default='')
    finish = models.BooleanField('是否完成', default=False)

