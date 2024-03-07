from django.urls import include, path
from . import views
from apps.cakes.views import CakeListView
from django.shortcuts import redirect
#

# urlpatterns = [
#     path('', CakeListView.as_view(), name='torts_list'),
#     path('about', views.about, name='about'),
# #
# urlpatterns = [
#     path('', CakeListView.as_view(), name='torts_list'),
#     # path('about.html', views, name='about'),
    # path('about.html', views.about, name='about'),

urlpatterns = [
    path('cakes/', CakeListView.as_view(), name='cake_list'),
    path('about/', views.about, name='about'),
]



def redirect_to_cakes(request):
    return redirect('cake_list')