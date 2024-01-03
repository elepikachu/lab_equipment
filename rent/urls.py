from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_view),
    path('detail/<int:item_id>', views.detail_view)
        ]