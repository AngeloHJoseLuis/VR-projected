import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VoiceChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("voice_chat", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("voice_chat", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Enviar mensaje a todos los usuarios en el grupo
        await self.channel_layer.group_send(
            "voice_chat",
            {
                "type": "chat_message",
                "message": message
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
