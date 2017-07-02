#-*- coding: utf-8 -*-
from django.db import models

#model Manager
class OriginItemPriceManager(models.Manager):
    def save_history(self,origin_id ,originprice,changedprice):
        try:
            tmporiginitem= OriginItem.objects.get(id = origin_id)
            tmporiginitemprice= OriginItemPriceHistory(originitem = tmporiginitem,originprice = originprice,changedprice = changedprice)
            tmporiginitemprice.save()
        except:
            tmporiginitemprice=None
        return tmporiginitemprice

class RoastItemPriceHistoryManager(models.Manager):
    def save_history(self,roast_id ,originprice,changedprice):
        try:
            tmproastitem= RoastItem.objects.get(id = roast_id)
            tmproastitempricehistory= RoastItemPriceHistory(roastitem = tmproastitem,originprice = originprice,changedprice = changedprice)
            tmproastitempricehistory.save()
        except:
            tmproastitempricehistory=None
        return tmproastitempricehistory

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length =20, verbose_name ='區域名稱')

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '生產區域'
        verbose_name_plural='生產區域'
        
        
class Process(models.Model):
    name = models.CharField(max_length =20,verbose_name='處理名稱')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = '處理方法'
        verbose_name_plural='處理方法'
        

    
class Country(models.Model):
    region= models.ForeignKey(Region)
    name = models.CharField(max_length =20,verbose_name ='國家名稱')
    description = models.TextField(default = '',verbose_name='國家說明')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '生產國家'
        verbose_name_plural='生產國家'
    
class Park(models.Model):
    country= models.ForeignKey(Country)
    engname = models.CharField(max_length =40,verbose_name ='莊園英文名稱')
    chinesename = models.CharField(max_length =40,verbose_name ='莊園中文名稱')
    description = models.TextField(default = '',verbose_name ='莊園說明')
    
    def __str__(self):
        return self.chinesename

        
        
    class Meta:
        verbose_name = '生產莊園'
        verbose_name_plural='生產莊園'
        
class Grade(models.Model):
    name = models.CharField(max_length =20,verbose_name='等級名稱')
    description = models.TextField(default = '',verbose_name='等級說明')
    
    def __str__(self):
        return self.name
        
        
    class Meta:
        verbose_name = '生豆分級'
        verbose_name_plural='生豆分級'
    

class OriginItem(models.Model):
    park= models.ForeignKey(Park)
    process= models.ForeignKey(Process)
    grade= models.ForeignKey(Grade)
    price = models.FloatField(default=0)
    engname = models.CharField(max_length =100,verbose_name='生豆英文名稱')
    chinesename = models.CharField(max_length =100,verbose_name='生豆中文名稱')
    description = models.TextField(default = '',verbose_name='生豆說明')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')

    objects = models.Manager()  # The default manager.

    def __str__(self):
        return self.chinesename

        
    class Meta:
        verbose_name = '生豆項目'
        verbose_name_plural='生豆項目'
        
    
class Roast(models.Model):
      name = models.CharField(max_length =20,verbose_name='焙度名稱')
      description = models.TextField(default = '',verbose_name='焙度說明')

      def __str__(self):
        return self.name
        
      class Meta:
        verbose_name = '烘焙焙度'
        verbose_name_plural='烘焙焙度'
        
        
class RoastItem(models.Model):
    LEVEL_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    originitem= models.ForeignKey(OriginItem)
    roast = models.ForeignKey(Roast)
    price = models.FloatField(default=0)
    aromadegree = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='香氣等級')
    sweetnessdegree = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='甜度等級')
    aciditydegree = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='酸味等級')
    bodydegree = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='醇厚等級')
    aftertastedegress = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='尾韻等級')
    balancedegress = models.IntegerField(choices=LEVEL_CHOICES,default=3,verbose_name='平衡等級')
    description = models.TextField(default = '',verbose_name='詳細說明')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')

    objects = models.Manager()  # The default manager.


    def __str__(self):
        return self.originitem.chinesename
        
        
    class Meta:
        verbose_name = '烘焙咖啡豆'
        verbose_name_plural='烘焙咖啡豆'


class OriginItemPriceHistory(models.Model):
    originitem= models.ForeignKey(OriginItem)
    originprice =  models.FloatField(default=0,verbose_name ='上次金額')
    changedprice =  models.FloatField(default=0,verbose_name ='修改金額')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')


    objects = models.Manager()  # The default manager.
    historyobjects =OriginItemPriceManager()


    class Meta:
        verbose_name = '生豆價格變動紀錄'
        verbose_name_plural='生豆價格變動紀錄'

class RoastItemPriceHistory(models.Model):
    roastitem= models.ForeignKey(RoastItem)
    originprice =  models.FloatField(default=0,verbose_name ='上次金額')
    changedprice =  models.FloatField(default=0,verbose_name ='修改金額')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')


    objects = models.Manager()  # The default manager.

    historyobjects =RoastItemPriceHistoryManager()


    class Meta:
        verbose_name = '熟豆價格變動紀錄'
        verbose_name_plural='熟豆價格變動紀錄'
        
    
    
    

    
        
        


      

    

    




    
        
        


    
    


    

    


