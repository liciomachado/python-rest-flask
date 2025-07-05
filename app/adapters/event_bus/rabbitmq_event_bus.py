import pika
import json
from app.domain.ports.event_bus import IEventBus

class RabbitMQEventBus(IEventBus):
    def __init__(self, host: str, username: str, password: str):
        credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, credentials=credentials)
        )
        self.channel = self.connection.channel()

    def publish(self, queue_name: str, payload: dict):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(payload),
            properties=pika.BasicProperties(
                delivery_mode=2,  # mensagem persistente
            )
        )

    def close(self):
        self.connection.close()
