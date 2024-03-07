# from django.urls import path
from django.urls import include, path

# from apps.products.views import ProductDetailView
from apps.products.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='flour_list'),
    # path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail')

]