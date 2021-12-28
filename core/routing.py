#route data to the consumer
from channels.auth import AuthMiddlewareStack  #for auuthentication .. we can use built in django auth 
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing

#if we have a ws request this is where to route it 

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),

})