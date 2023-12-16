
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from ..api.consumers import Chat

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', Chat.as_asgi()),
    ]),
})
