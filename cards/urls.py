
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="home"),

    path('create-set/', views.create_set, name="create_set"),
    path('update-set/<int:pk>/', views.update_set, name="update_set"),
    path('delete-set/<int:pk>/', views.delete_set, name="delete_set"),
    path('set-cards/<int:pk>/', views.individual_set, name="set_cards"),

    path('all-cards/', views.all_cards, name="all_cards"),
    path('add-card/', views.add_cards, name="add_card"),
    path('update-card/<int:pk>/', views.edit_card, name="edit_card"),
    path('delete-card/<int:pk>/', views.delete_card, name="delete_card"),

    path('box-cards/<str:pk>/<int:box_num>/',
         views.box_view, name="box_cards"),
    path('all-box-cards/<int:box_num>/',
         views.all_box_view, name="all_box_cards"),
]
