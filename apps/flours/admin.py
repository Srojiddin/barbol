from django.contrib import admin


from apps.flours.models import Flour, FlourImage


class FlourImageInline(admin.TabularInline):
    model = FlourImage
    extra = 1


@admin.register(FlourImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Flour)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'price']
    search_fields = ['title']
    inlines = [FlourImageInline]