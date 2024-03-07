from django import forms
from apps.cart.models import Favorite


class AddToFavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = []