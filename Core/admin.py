from django.contrib import admin
from .models import Shop, Service, ShopASIC, ASIC, ShopAccessories, Accessories

class ShopASICInline(admin.TabularInline):
    model = ShopASIC


class ShopAccInline(admin.TabularInline):
    model = ShopAccessories

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # list_display = ['Description', 'dateLast']
    # fields = ['Description', 'dateLast']
    inlines = [ShopASICInline, ShopAccInline]

admin.site.register(Accessories)

admin.site.register(Service)
admin.site.register(ASIC)