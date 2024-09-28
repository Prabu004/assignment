from channels.generic.websocket import WebsocketConsumer
import json

class MachineDataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        response = {'message': 'Received data for machine', 'data': data}
        self.send(text_data=json.dumps(response))
