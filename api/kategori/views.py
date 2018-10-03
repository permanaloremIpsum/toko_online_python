from rest_framework import generics
from produk.models import Kategori
from api.kategori.serializers import KategoriSerializer
from api.permissions import IsAdminOrReadOnly


class KategoriList(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = (IsAdminOrReadOnly,)

class KategoriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = (IsAdminOrReadOnly,)