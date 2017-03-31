from django.contrib import admin
from .models import Timer, City, Building
# Register your models here.

class BuildingInline(admin.TabularInline):
    model = Building
    
class BuildingAdmin(admin.ModelAdmin):
    readonly_fields = ('building_id',)
    list_display = ('building_name','building_city_name')

    def building_city_name(self, obj):
        return obj.city.city_name
    building_city_name.admin_order_field  = 'city'  #Allows column order sorting
    building_city_name.short_description = 'City name'  #Renames column head

class CityAdmin(admin.ModelAdmin):
    inlines = [
        BuildingInline,
    ]
    list_display = ('city_name',)


admin.site.register(Timer, admin.ModelAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Building, BuildingAdmin)