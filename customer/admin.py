#-*- coding: utf-8 -*-
from django.contrib import admin
from customer.models import Customer,MoneyCardType,CustomerMoneyCard,CustomerCardSaveHistory
# Register your models here
import sys
import datetime
import decimal

reload(sys)
sys.setdefaultencoding('utf8')

class CustomerAdmin(admin.ModelAdmin):

    list_display=("id","name","phone","email","createdtime")

    search_fields =('name','phone')
    ordering = ('id',)


class CustomerMoneyCardAdmin(admin.ModelAdmin):

    list_display=("id","customer_name","customer_phone","card_type","addmoney","lastedmoney","currentmoney","createdtime","lastupdatedtime")
    readonly_fields = ['lastedmoney', 'currentmoney']
    list_filter =('cardtype__name',)
    search_fields =('customer__name','customer__phone')
    ordering = ('id',)

    def customer_name(self,obj):
        return obj.customer.name
    customer_name.short_description = '客戶名稱'

    def customer_phone(self,obj):
        return obj.customer.phone
    customer_phone.short_description = '客戶電話'

    def card_type(self,obj):
        return obj.cardtype.name
    card_type.short_description = '卡片名稱'


    def save_model(self, request, obj, form, change):
        if change and 'addmoney' in form.changed_data:
            currentvalue = float(obj.currentmoney)
            newvalue = form.cleaned_data.get('addmoney')
            obj.lastedmoney = newvalue
            obj.currentmoney = currentvalue + newvalue
            obj.lastupdatedtime = datetime.datetime.now()
            obj.addmoney = 0
            CustomerCardSaveHistory.historyobjects.save_history(obj.id,newvalue)
        super(CustomerMoneyCardAdmin, self).save_model(request, obj, form, change)


class CustomerCardSaveHistoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(CustomerCardSaveHistoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


    list_display=("id","customer_name","customer_phone","card_type","addmoney","createdtime")
    search_fields =('customercard__customer__name','customercard__customer__phone')
    list_filter =('customercard__cardtype__name',)
    readonly_fields = ['addmoney']
    ordering = ('createdtime',)

    list_display_links = None


    def customer_name(self,obj):
        return obj.customercard.customer.name
    customer_name.short_description = '客戶名稱'


    def customer_phone(self,obj):
        return obj.customercard.customer.phone
    customer_phone.short_description = '客戶電話'


    def card_type(self,obj):
        return obj.customercard.cardtype.name
    card_type.short_description = '卡片名稱'





admin.site.register(Customer,CustomerAdmin)
admin.site.register(MoneyCardType)
admin.site.register(CustomerMoneyCard,CustomerMoneyCardAdmin)
admin.site.register(CustomerCardSaveHistory,CustomerCardSaveHistoryAdmin)



