from django.contrib import admin
# Register your models here.
from api.models import ProductoPequeno, ProductoMediano, ProductoGrande, ProductoGigante

admin.site.register(ProductoPequeno)
admin.site.register(ProductoMediano)
admin.site.register(ProductoGrande)
admin.site.register(ProductoGigante)