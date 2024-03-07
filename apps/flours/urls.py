from django.urls import include, path

from apps.flours.views import FlourListView

urlpatterns = [
    path('', FlourListView.as_view(), name='flour_list'),

]