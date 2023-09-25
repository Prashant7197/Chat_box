from django.urls import path
from .import views
from .views import MessageListCreateView

urlpatterns = [
    path('', views.chat, name="chat"),  
    path('api/messages/', MessageListCreateView.as_view(), name='message-list-create'), 
    # path('create_message/', views.create_message_with_attachment, name='create_message'),
]
