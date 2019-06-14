from django.db import models
from django.urls import reverse  # generate urls from url patterns


# Create your models here.



class Category (models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a product category (e.g. Coffee Bean, Drink, Cake, Souvenir etc.)"
    )
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True, unique=True)
    image = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=10)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def checkavailability (self):
        if self.stock ==0:
            self.available = False

        return self.available

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
