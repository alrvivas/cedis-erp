import uuid
from django.urls import reverse
from django.db import models
from cedis.models import Cedis, Route
from price_list.models import PriceList


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Employee(AbstractModel):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, verbose_name=('Slug'))
    cedis = models.ForeignKey(
        Cedis, on_delete=models.CASCADE, null=True, blank=True)
    price_lists = models.ManyToManyField(PriceList, null=True, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    BILLING_CONDITIONS = (
        ('CTDO', 'Contado'),
        ('CRED', 'Credito'),
    )
    name = models.CharField(max_length=140, verbose_name=('Razón Social'))
    slug = models.SlugField(unique=True, null=True,
                            blank=True, verbose_name=('Slug'))
    manager = models.CharField(max_length=140, null=True, blank=True)
    rfc = models.CharField(max_length=20, null=True, blank=True)
    call_visit = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=('Llamada/Visita'))
    billing_condition = models.CharField(
        max_length=4, choices=BILLING_CONDITIONS, null=True, blank=True)
    route = models.ForeignKey(
        Route, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    price_list = models.ForeignKey(
        PriceList, on_delete=models.CASCADE, null=True, blank=True)
    tel_1 = models.CharField(max_length=50, null=True, blank=True)
    tel_2 = models.CharField(max_length=50, null=True, blank=True)
    cel = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person:person_detail', args=[str(self.slug)])
