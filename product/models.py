# -*- coding: utf-8 -*-

from django.db import models


#model Manager
class ProductPriceHistoryManager(models.Manager):
    def save_history(self,product_id ,originprice,changedprice):
        try:
            tmpproductitem= ProductItem.objects.get(id = product_id)
            tmpproductpricehistory= ProductPriceHistory(productitem = tmpproductitem,originprice = originprice,changedprice = changedprice)
            tmpproductpricehistory.save()
        except:
            tmpproductpricehistory=None
        return tmpproductpricehistory

# Create your models here.
class ProductUnit(models.Model):
    name = models.CharField(max_length =20,verbose_name='產品單位') 

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name ='單位名稱'
        verbose_name_plural='單位名稱'
        
class ProductType(models.Model):
    name = models.CharField(max_length=30,verbose_name='產品類型')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='類型名稱'
        verbose_name_plural='類型名稱'
        
class ProductItem(models.Model):
    productunit= models.ForeignKey(ProductUnit)
    producttype = models.ForeignKey(ProductType)
    name = models.CharField(max_length=30,verbose_name='產品名稱')
    price = models.IntegerField(default=0,verbose_name='產品價格')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= '產品項目'
        verbose_name_plural='產品項目'
        
class ProductPriceHistory(models.Model):
    productitem= models.ForeignKey(ProductItem)
    originprice =  models.FloatField(default=0,verbose_name ='上次金額')
    changedprice =  models.FloatField(default=0,verbose_name ='修改金額')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')


    objects = models.Manager()  # The default manager.

    historyobjects =ProductPriceHistoryManager()


    class Meta:
        verbose_name = '產品價格變動紀錄'
        verbose_name_plural='產品價格變動紀錄'


    
    

    
        



