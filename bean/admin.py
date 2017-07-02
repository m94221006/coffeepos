#-*- coding: utf-8 -*-

from django.contrib import admin
from bean.models import Region,Process,Country,Park,Grade,OriginItem,Roast,RoastItem ,OriginItemPriceHistory,RoastItemPriceHistory
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Register your models here.
class ParkAdmin(admin.ModelAdmin):
    
    list_display=("id","region_name",)
    
    search_fields =('name',)
    ordering = ('name',)

    def region_name(self,obj):
        return obj.country.region.name
        
    def country_name(self,obj):
        return obj.country.name
        
        

class OriginItemAdmin(admin.ModelAdmin):


    list_display=("id","park_country","park_chinesename","process_name"
     ,"grade_name","engname","chinesename","price","description")
     
    search_fields =('chinesename',)
    ordering = ('id',)


    
    def park_country(self,obj):
        return obj.park.country.name
     
    def park_chinesename(self,obj):
        return obj.park.chinesename
        
    def process_name(self,obj):
        return obj.process.name
        
    def grade_name(self,obj):
        return obj.grade.name

    def save_model(self, request, obj, form, change):
        if change and 'price' in form.changed_data:
            currentvalue =  OriginItem.objects.get(id = obj.id).price
            newvalue = form.cleaned_data.get('price')
            if currentvalue!= newvalue:
                OriginItemPriceHistory.historyobjects.save_history(obj.id,currentvalue,newvalue)
        super(OriginItemAdmin, self).save_model(request, obj, form, change)


        
class RoastItemAdmin(admin.ModelAdmin):
    list_display=("id","origin_chinesename","roast_name","price","degree_description","description")
      
    search_fields =('origin_chinesename',)
    ordering = ('id',)
      
    def origin_chinesename(self,obj):
          return obj.originitem.chinesename
          
    def roast_name(self,obj):
          return obj.roast.name
          
    def degree_description(self,obj):
          description = u"香氣：%s , 甘度：%s , 酸度 :%s , 醇厚 :%s , 尾韻 :%s , 平衡 :%s"%(obj.aromadegree,obj.sweetnessdegree,
                        obj.aciditydegree,obj.bodydegree,obj.aftertastedegress,obj.balancedegress)
          return description

    def save_model(self, request, obj, form, change):
        if change and 'price' in form.changed_data:
            currentvalue =  RoastItem.objects.get(id = obj.id).price
            newvalue = form.cleaned_data.get('price')
            if currentvalue!= newvalue:
                RoastItemPriceHistory.historyobjects.save_history(obj.id,currentvalue,newvalue)
        super(RoastItemAdmin, self).save_model(request, obj, form, change)


          
          
class OriginItemPriceHistoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(OriginItemPriceHistoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display=("id","park_region","park_country","park_name","origin_chinesename","origin_processname","originprice","changedprice","createdtime")
    search_fields =('originitem__chinesename',)
    list_filter =('originitem__park__country__region__name',)
    ordering = ('createdtime',)

    list_display_links = None


    def park_region(self,obj):
        return obj.originitem.park.country.region.name
    park_region.short_description = '莊園區域'


    def park_country(self,obj):
        return obj.originitem.park.country.name
    park_country.short_description = '莊園國家'


    def park_name(self,obj):
        return obj.originitem.park.chinesename
    park_name.short_description = '莊園名稱'


    def origin_chinesename(self,obj):
        return obj.originitem.chinesename
    origin_chinesename.short_description = '豆子名稱'

    def origin_processname(self,obj):
        return obj.originitem.process.name
    origin_processname.short_description = '處理方式'



class RoastItemPriceHistoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(RoastItemPriceHistoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display=("id","origin_park_name","origin_chinesename","roast_name","originprice","changedprice","createdtime")
    search_fields =('roastitem__originitem__chinesename',)
    list_filter =('roastitem__originitem__park__country__region__name',)
    ordering = ('createdtime',)

    list_display_links = None

    def origin_park_name(self,obj):
        return obj.roastitem.originitem.park.chinesename
    origin_park_name.short_description = '莊園名稱'

    def origin_chinesename(self,obj):
        return obj.roastitem.originitem.chinesename
    origin_chinesename.short_description = '豆子名稱'

    def roast_name(self,obj):
        return obj.roastitem.roast.name
    roast_name.short_description = '焙度'




admin.site.register(Region)
admin.site.register(Process)
admin.site.register(Country)
admin.site.register(Park)
admin.site.register(Grade)
admin.site.register(Roast)
admin.site.register(OriginItem,OriginItemAdmin)
admin.site.register(RoastItem,RoastItemAdmin)
admin.site.register(OriginItemPriceHistory,OriginItemPriceHistoryAdmin)
admin.site.register(RoastItemPriceHistory,RoastItemPriceHistoryAdmin)




        
        
        
        
        
        
     