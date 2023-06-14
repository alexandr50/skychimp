
from django.urls import path

from sending.views import CreateMessage, DetailMessage, ListMessages, UpdateMessage, DeleteMessage, ListSending, \
    CreateSending, DetailSending

app_name = 'sending'

urlpatterns = [
    path('create_message/', CreateMessage.as_view(), name='create_message'),
    path('detail_message/<int:pk>/', DetailMessage.as_view(), name='detail_message'),
    path('list_messages/', ListMessages.as_view(), name='list_messages'),
    path('update_message/<int:pk>/', UpdateMessage.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', DeleteMessage.as_view(), name='delete_message'),
    path('list_sending/', ListSending.as_view(), name='list_sending'),
    path('create_sending/', CreateSending.as_view(), name='create_sending'),
    path('detail_sending/<int:pk>/', DetailSending.as_view(), name='detail_sending'),

]