from django.urls import path, re_path
from api.order.views import OrderList

urlpatterns = [
	path('', OrderList.as_view(), name='order-list'),
	# re_path(r'^(?P<pk>[0-9]+)/$', OrderDetail.as_view(), name='order-detail'),
]