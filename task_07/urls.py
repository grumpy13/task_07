
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.welcome ,name='hello-world'),
    path('restaurants/list/',views.restaurant_list ,name='restaurant-list'),
    path('restaurants/detail/<int:restaurant_id>/',views.restaurant_detail ,name='restaurant-detail'),

    path('restaurants/create/',views.restaurant_create ,name='restaurant-create'),
    path('restaurants/update/<int:restaurant_id>/',views.restaurant_update ,name='restaurant-update'),
    path('restaurants/delete/<int:restaurant_id>/',views.restaurant_delete ,name='restaurant-delete'),
]
