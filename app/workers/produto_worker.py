import pika
import json
from app.config import Config

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"[x] Produto criado: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_worker():
    credentials = pika.PlainCredentials(Config.RABBITMQ_USER, Config.RABBITMQ_PASSWORD)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=Config.RABBITMQ_HOST,
            credentials=credentials
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue='produto_criado', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='produto_criado', on_message_callback=callback)

    print('[*] Aguardando mensagens. CTRL+C para sair')
    channel.start_consuming()

if __name__ == "__main__":
    start_worker()
