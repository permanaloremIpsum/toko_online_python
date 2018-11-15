from rest_framework import generics, permissions
from produk.models import Produk
from api.produk.serializers import ProdukSerializer
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'kategori': ['exact'],
        'merk': ['iexact'],
        'harga': ['gte', 'lte']
    }

class ProdukDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (IsAdminOrReadOnly,)