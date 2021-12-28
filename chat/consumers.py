import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):

    #call this fct that return result when you awaiting me
    #connect to websoket or initiate it
    async def connect(self):
        #capture the room name from url
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #All users go in this urls put them inside a same group 
        print(self.room_name)
        self.room_group_name ='chat_%s' % self.room_name 
        print(self.room_group_name)

        await self.channel_layer.group_add(
          self.room_group_name  ,
          self.channel_name  #contain a pointer to the channel layer insatnce and the channel name that will reach the consumer
        )

        await self.accept()
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     #message to send
        #     {
        #         'type':'tester_message',
        #         'tester':'hello world welcome '
        #     }
        # )
        #during the handshake process our application should accept or reject this connection 

    # async def tester_message(self,event):
    #     #collect data from group_send
    #     tester = event['tester']
    #     #send it across websoket
    #     await self.send(text_data = json.dumps({
    #         'tester':tester,
    #     }))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name #channel to remove 
        )

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # after collect data ,send data to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chatroom_message',
                'message':message,
                'username':username
            }
        )
    #now we are gonna send the message to the websocket 
    async def chatroom_message(self,event):
        message = event['message']
        username = event['username']
            
        await self.send(text_data = json.dumps({
            'message':message,
            'username':username
        }))


    pass
