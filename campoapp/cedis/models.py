import uuid
from django.urls import reverse
from django.db import models
from product.models import Product, MixedProduct


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cedis(AbstractModel):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, verbose_name=('Slug'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cedis:cedis_detail', args=[str(self.slug)])

    def add_route_url(self):
        return ('cedis:new_route', (), {'slug': self.slug})


class Route(AbstractModel):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, verbose_name=('Slug'))
    cedis = models.ForeignKey(
        Cedis, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cedis:route_detail', args=[str(self.slug)])


class CedisProduct(models.Model):
    cedis = models.ForeignKey(
        Cedis, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)

    def get_name_cedis(self):
        return self.cedis.name + "-" + self.product.name

    def __str__(self):
        return self.product.name


class MixedProduct(models.Model):
    cedis = models.ForeignKey(
        Cedis, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(MixedProduct, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)

    def get_name(self):
        return self.product.name

    def __str__(self):
        return self.product.name


class Promotion(AbstractModel):
    product = models.ForeignKey(CedisProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, verbose_name=('Nombre'))
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    discount = models.DecimalField(
        max_digits=30, decimal_places=3, verbose_name=('Discount %'))
    condition = models.IntegerField(
        null=True, blank=True, verbose_name=('Condition >= '))
    description = models.TextField(max_length=255, )

    def __str__(self):
        return self.name
