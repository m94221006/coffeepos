#-*- coding: utf-8 -*-
from django.db import models

#model Manager
class CustomerCardSaveHistoryManager(models.Manager):
    def save_history(self,customer_card_id ,lastedmoney):
        try:
            tmpcustomercard= CustomerMoneyCard.objects.get(id = customer_card_id)
            tmpcustomerhistory= CustomerCardSaveHistory(customercard = tmpcustomercard,addmoney = lastedmoney)
            tmpcustomerhistory.save()
        except:
            tmpcustomerhistory=None
        return tmpcustomerhistory

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50,verbose_name ='名字')
    phone = models.CharField(max_length=50,verbose_name ='電話')
    email = models.CharField(max_length=50,verbose_name ='電子郵件')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')


    objects = models.Manager()  # The default manager.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客戶列表'
        verbose_name_plural='客戶列表'

class MoneyCardType(models.Model):
    name = models.CharField(max_length=30 ,verbose_name ='類型名稱')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '儲值卡類型'
        verbose_name_plural='儲值卡類型'

class CustomerMoneyCard(models.Model):
    customer =  models.ForeignKey(Customer)
    cardtype= models.ForeignKey(MoneyCardType)
    addmoney  = models.FloatField(default=0,verbose_name ='新增金額')
    lastedmoney  = models.FloatField(default=0,verbose_name ='上次新增金額')
    currentmoney = models.FloatField(default=0,verbose_name ='目前金額')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')
    lastupdatedtime= models.DateTimeField(auto_now_add=True,verbose_name ='最後更新時間')


    objects = models.Manager()  # The default manager.

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = '客戶儲值列表'
        verbose_name_plural='客戶儲值列表'


class CustomerCardSaveHistory(models.Model):
    customercard= models.ForeignKey(CustomerMoneyCard)
    addmoney =  models.FloatField(default=0,verbose_name ='新增金額')
    createdtime =  models.DateTimeField(auto_now_add=True,verbose_name ='建立時間')


    objects = models.Manager()  # The default manager.

    historyobjects =CustomerCardSaveHistoryManager()


    class Meta:
        verbose_name = '客戶儲值紀錄'
        verbose_name_plural='客戶儲值紀錄'


























    
    
