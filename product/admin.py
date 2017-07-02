#-*- coding: utf-8 -*-


from django.contrib import admin
from product.models import ProductUnit,ProductType,ProductItem,ProductPriceHistory

import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Register your models here.
class ProductItemAdmin(admin.ModelAdmin):

    list_display=("id","unit_name","type_name","name","price","createdtime")
    list_filter =('producttype__name',)

    search_fields =('name',)
    ordering = ('createdtime',)

    def unit_name(self,obj):
        return obj.productunit.name
    unit_name.short_description = '單位'


    def type_name(self,obj):
        return obj.producttype.name
    type_name.short_description = '類型'


    def save_model(self, request, obj, form, change):
        if change and 'price' in form.changed_data:
            currentvalue =  ProductItem.objects.get(id = obj.id).price
            newvalue = form.cleaned_data.get('price')
            if currentvalue!= newvalue:
                ProductPriceHistory.historyobjects.save_history(obj.id,currentvalue,newvalue)
        super(ProductItemAdmin, self).save_model(request, obj, form, change)



class ProductPriceHistoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(ProductPriceHistoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display=("id","product_name","type_name","unit_name","originprice","changedprice","createdtime")
    search_fields =('productitem__name',)
    list_filter =('productitem__producttype__name',)
    ordering = ('createdtime',)

    list_display_links = None

    def product_name(self,obj):
        return obj.productitem.name
    product_name.short_description = '名稱'

    def unit_name(self,obj):
        return obj.productitem.productunit.name
    unit_name.short_description = '單位'


    def type_name(self,obj):
        return obj.productitem.producttype.name
    type_name.short_description = '類型'



admin.site.register(ProductUnit)
admin.site.register(ProductType)
admin.site.register(ProductItem,ProductItemAdmin)
admin.site.register(ProductPriceHistory,ProductPriceHistoryAdmin)


