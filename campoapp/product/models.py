import uuid
from django.db import models

class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
	name = models.CharField(max_length=140)	
	slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))	
	orden = models.PositiveIntegerField(null=True, blank=True)
	#def imagen_categoria(self):
	#	return """<img src="%s" style="width:8em;" />""" % self.imagen.url

	#imagen_categoria.allow_tags = True

	class Meta:
		ordering = ['orden']
		verbose_name_plural = 'Categorias' 

	def __str__(self): 
		return self.name

	#@models.permalink
	#def get_absolute_url(self):
	#	return ('catalogo_categoria', (), { 'categoria_slug': self.slug })

class Product(AbstractModel):
	UNIDAD = (
        ('Cj', 'Caja'),
        ('Pz', 'Pieza'),
    )
	name = models.CharField(max_length=140, verbose_name=('Nombre'))
	slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))
	barcode = models.CharField(max_length=20, unique=True,default=None,null=True, blank=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
	standard_price = models.DecimalField(max_digits = 30,decimal_places = 3,verbose_name=('Precio Estandar'))
	weight = models.DecimalField(max_digits = 30,decimal_places = 3,)
	unit = models.CharField(max_length=2, choices=UNIDAD)	

	def __str__(self): 
		return self.name

class MixedProduct(AbstractModel):
	name = models.CharField(max_length=140, verbose_name=('Nombre'))
	slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))
	barcode = models.CharField(max_length=20, unique=True,null=True, blank=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
	standard_price = models.DecimalField(max_digits = 30,decimal_places = 3,verbose_name=('Precio Estandar'))
	weight = models.DecimalField(max_digits = 30,decimal_places = 3,)

	def __str__(self): 
		return self.name

class MProducts(models.Model):
	mixedproduct = models.ForeignKey(MixedProduct,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.IntegerField(null=True, blank=True)

	def get_name(self):
		return self.product.name

	def __unicode__(self): 
		return unicode(self.product)

    