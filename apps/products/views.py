from django.views import generic
from django.shortcuts import render
from apps.products.models import Product

#
class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
#
        context['left_categories'] = Product.objects.filter(parent=None)
#         # context['palto_products'] = Product.objects.filter(category__title="Пальто")[:4]
#         # context['shtany_products'] = Product.objects.filter(category__title="Штаны")[:4]
#         # context['crossy_products'] = Product.objects.filter(category__title="Кроссы")[:4]
        context['flour_products'] = Product.objects.all()

#
# def about(request):
#     return render(request, 'about.html')
#
#
# # class ProductDetailView(generic.DetailView):
# #     model = Product
# #     slug_field = 'slug'
# #     template_name = 'detail.html'