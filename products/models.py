from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT_CHOICES = [
        ('unit', 'per Unit'),
        ('meter', 'per Meter'),
        ('kg', 'per KG'),
        ('piece', 'per Piece'),
        ('sqft', 'per Sq.Ft'),
        ('roll', 'per Roll'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=20, choices=UNIT_CHOICES, default='unit')
    description = models.TextField()
    extra_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.product.name} Image"