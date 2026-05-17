from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    min_num = 1
    max_num = 10
    can_delete = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'units', 'in_stock')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'material', 'description')

    inlines = [ProductImageInline]

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category', 'material', 'price', 'units', 'in_stock')
        }),
        ('Variants', {
            'fields': ('colors', 'dimensions', 'available_sizes'),
            'description': (
                'Enter comma-separated values.<br>'
                '<b>Colors</b> e.g: Brown,Black,White<br>'
                '<b>Dimensions</b> e.g: 60x30x45cm, 90x40x75cm<br>'
                '<b>Available Sizes</b> e.g: 7ft,8ft,9ft,10ft — '
                'add * to mark out of stock: 7ft,8ft,9ft*,10ft'
            )
        }),
        ('Description', {
            'fields': ('description', 'extra_info')
        }),
        ('Main Image', {
            'fields': ('image',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)