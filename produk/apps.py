from django.apps import AppConfig


class ProdukConfig(AppConfig):
    name = 'produk'

    def ready(self):
        import produk.signals
