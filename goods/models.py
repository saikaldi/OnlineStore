from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='discount in %')
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return f'{self.name} Quantity-{self.quantity}'

    class Meta:
        db_table = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('id',)


    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price