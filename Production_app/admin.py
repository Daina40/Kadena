from django.contrib import admin
from Production_app.models import ProductionModel

@admin.register(ProductionModel)
class ProductionAdmin(admin.ModelAdmin):
    list_display = [
        'floor',
        'line', 
        'buyer',
        'style',
        'item',
        'po_buy',
        'order_qty', 
        'daily_prod', 
        'total_prod', 
        'daily_insp', 
        'total_insp', 
        'daily_packpass', 
        'total_packpass', 
        'line_balance', 
        'insp_balance', 
        'total_balance',
        'remarks'
    ]
