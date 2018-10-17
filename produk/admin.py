from django.contrib import admin
from .models import Kategori, Produk, Order, OrderBarang
# Register your models here.

class ProdukInline(admin.TabularInline):
	model = Produk

class KategoriAdmin(admin.ModelAdmin):
	inline = [
		ProdukInline,
	]


class OrderBarangInline(admin.TabularInline):
	model = OrderBarang

class OrderAdmin(admin.ModelAdmin):
	inlines = [
		OrderBarangInline,
	]


admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Produk)
admin.site.register(Order, OrderAdmin)