from django.views import generic
from django.shortcuts import render, redirect

from apps.cart.models import Cart, Item

from apps.cart.models import Favorite
from apps.cart.forms import AddToFavoriteForm


class CartDetailView(generic.ListView):
    template_name = 'cart-detail.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)


class QuantityChangeLogics:

    @staticmethod
    def minus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        if item.quantity -1 == 0:
            item.delete()
            return redirect('cart')
        item.quantity -= 1
        item.save()
        return redirect('cart')

    def plus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')





def add_to_favorite(request, product_id):
    if request.method == 'POST':
        form = AddToFavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.user = request.user
            favorite.product_id = product_id
            favorite.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = AddToFavoriteForm()
    return render(request, 'add_to_favorite.html', {'form': form})


def remove_from_favorite(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.delete()
    return redirect('favorites_list')