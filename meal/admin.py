from django.contrib import admin
from . models import Meals, Reservation
# Register your models here.


admin.site.register(Reservation)


class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_tag', 'price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Meals, MealAdmin)