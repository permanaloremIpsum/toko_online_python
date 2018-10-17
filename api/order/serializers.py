from rest_framework import serializers
from produk.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'no_hp',
            'alamat',
            'ongkir',
            'catatan',
            'date',
            'status',
            'totalbelanja', 
        )