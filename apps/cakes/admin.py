
from django.contrib import admin


from apps.cakes.models import Cake, CakeImage


class CakeImageInline(admin.TabularInline):
    model = CakeImage
    extra = 1


@admin.register(CakeImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Cake)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'price']
    search_fields = ['title']
    inlines = [CakeImageInline]

