from django.contrib import admin
from .models import Customer,Recieve,Item,Sell
from django.contrib.admin import ModelAdmin

class Cus(ModelAdmin):
    model=Customer
    list_display=["cus_id","sei","mei",]

class Rec(ModelAdmin):
    model=Recieve
    list_display=["rec_id","rec_no","rec_ver","rec_cus_id"]

class It(ModelAdmin):
    model=Item
    list_display=["item_rec_id","item_name"]

class Se(ModelAdmin):
    model=Sell
    list_display=["sell_cus_id","sell_mon","sell_money"]

admin.site.register(Customer,Cus) 
admin.site.register(Recieve,Rec)
admin.site.register(Item,It)
admin.site.register(Sell,Se)