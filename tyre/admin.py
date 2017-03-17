from django.contrib import admin
from .models import Symbol, Capacity, Speed, Label, Companies

class SymbolAdmin(admin.ModelAdmin):
    search_fields = ['symbol']
    list_display = ('symbol', 'description')
    list_filter = ['symbol']
    ordering = ('symbol',)
    
class CapacityAdmin(admin.ModelAdmin):
    search_fields = ['symbol']
    list_display = ('symbol', 'capacity')
    list_filter = ['symbol']
    ordering = ('id',)
    
class SpeedAdmin(admin.ModelAdmin):
    search_fields = ['symbol']
    list_display = ('symbol', 'speed')
    list_filter = ['symbol']
    ordering = ('symbol',)
    
class LabelAdmin(admin.ModelAdmin):
    search_fields = ['symbol']
    list_display = ('symbol', 'rollingResistance', 'wetGrip', 'externalNoise')
    list_filter = ['symbol']
    ordering = ('symbol',)

class CompaniesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'brands')
    list_display = ('name', 'headquarters', 'brands', 'factory')
    list_filter = ['name']
    ordering = ('name',)

    
admin.site.register(Symbol, SymbolAdmin),
admin.site.register(Capacity, CapacityAdmin),
admin.site.register(Speed, SpeedAdmin),
admin.site.register(Label, LabelAdmin),
admin.site.register(Companies, CompaniesAdmin),