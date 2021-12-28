from django.urls import re_path  #more advanced paths to capture the urls
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer.as_asgi()),

]