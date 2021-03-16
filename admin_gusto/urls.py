from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', list_of_messages, name='list_of_messages'),
    path("messages/update/<int:pk>/", update_message, name ="update_message"),

    path("categories/", list_of_categories, name = "list_of_categories"),
    path("categories/add", CategoryAddView.as_view(), name = "categories_add"),
    path("categories/delete/<int:pk>/", CategoryDeleteView.as_view(), name = "categories_delete"),
    path("categories/update/<int:pk>/", CategoryUpdateView.as_view(), name = "categories_update")]