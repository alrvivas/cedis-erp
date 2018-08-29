import uuid
from django.db import models
from cedis.models import Cedis,CedisProduct,MixedProduct

class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class PriceList(AbstractModel):
	cedis = models.ForeignKey(Cedis,on_delete=models.CASCADE)
	name = models.CharField(max_length=255, verbose_name=('Nombre'))
	slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))

	def __str__(self): 
		return self.name


class ProductList(models.Model):
	price_list = models.ForeignKey(PriceList,on_delete=models.CASCADE)
	product = models.ForeignKey(CedisProduct,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits = 30,decimal_places = 3,verbose_name=('Precio'))

	def get_name_cedis(self):
		return self.price_list.cedis.name +"-"+ self.product.product.name

	def __str__(self): 
		return self.product.cedis.name +"-"+ self.product.product.name

class MixedProductList(models.Model):
	price_list = models.ForeignKey(PriceList,on_delete=models.CASCADE)
	product = models.ForeignKey(MixedProduct,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits = 30,decimal_places = 3,verbose_name=('Precio'))

	def __unicode__(self): 
		return unicode(self.product.name)