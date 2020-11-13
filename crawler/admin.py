from django.contrib import admin
from .models import Sale
# Register your models here.
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'image', 'discount', 'price', 'sale_date')
    list_per_page = 25

admin.site.register(Sale, SaleAdmin)