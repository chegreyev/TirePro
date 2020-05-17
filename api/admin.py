from django.contrib import admin
from .models import *

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    pass

@admin.register(Disc)
class DiscAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass