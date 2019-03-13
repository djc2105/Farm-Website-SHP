from django.contrib import admin
from website.models import Row,Plant, Lot

# Register your models here.


class LotAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class RowAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PlantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Plant)
admin.site.register(Row)
admin.site.register(Lot)
