from django.contrib import admin


from .models import Cliente,Pagos, Seguimiento

admin.site.register({Cliente, Pagos, Seguimiento})
# Register your models here.
