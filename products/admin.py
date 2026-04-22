from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    min_num = 1
    max_num = 10
    can_delete = True


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price','units')
    list_filter = ('category',)
    search_fields = ('name', 'material', 'description')

    inlines = [ProductImageInline]

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category', 'material', 'price','units')
        }),
        ('Description', {
            'fields': ('description', 'extra_info')
        }),
        ('Main Image', {
            'fields': ('image',)
        }),
    )


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)