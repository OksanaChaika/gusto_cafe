from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', list_of_messages, name='list_of_messages'),
    path("messages/update/<int:pk>/", update_message, name ="update_message")

]