from django.urls import path
from apps.cart.views import CartDetailView, QuantityChangeLogics
from .views import add_to_favorite, remove_from_favorite

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart'),
    path('minus/<int:pk>', QuantityChangeLogics.minus_quantity, name='minus_quantity'),
    path('plus/<int:pk>', QuantityChangeLogics.plus_quantity, name='plus_quantity'),
    path('product/<int:product_id>/add-to-favorite/', add_to_favorite, name='add_to_favorite'),
    path('favorite/<int:favorite_id>/remove/', remove_from_favorite, name='remove_from_favorite'),
]