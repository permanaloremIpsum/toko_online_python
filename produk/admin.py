from django.contrib import admin
from .models import Kategori, Produk
# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
	list_display = ('nama',)


class ProdukAdmin(admin.ModelAdmin):
	list_display = ('nama','merk','harga','qty',)

admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Produk,ProdukAdmin)