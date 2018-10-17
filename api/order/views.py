from rest_framework import generics, permissions
from produk.models import Order
from api.order.serializers import OrderSerializer
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = (permissions.IsAuthenticated,)