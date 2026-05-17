from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    extra_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    colors = models.CharField(
        max_length=300, blank=True, null=True,
        help_text="Comma-separated e.g. Brown,Black,White"
    )
    dimensions = models.CharField(
        max_length=300, blank=True, null=True,
        help_text="Comma-separated e.g. 60x30x45cm, 90x40x75cm, 120x50x90cm"
    )
    available_sizes = models.CharField(
    max_length=300, blank=True, null=True,
    help_text="Format: size:price — e.g. 7ft:5000,8ft:6500,9ft:8000,10ft:9500 — add * for out of stock: 9ft*:8000"
)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.product.name} Image"