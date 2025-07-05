import pika
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from app.config import Config

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Executor com 10 threads paralelas
executor = ThreadPoolExecutor(max_workers=10)

def process_message(body, ch, method):
    try:
        data = json.loads(body)
        logger.info(f"[✓] Processando produto: {data}")

        # Simule processamento aqui (ex: salvar no banco, validações etc.)
        # TODO: Chamar service de produto se necessário

        ch.basic_ack(delivery_tag=method.delivery_tag)
        logger.info("[✓] Mensagem processada com sucesso")

    except Exception as e:
        logger.exception(f"[x] Erro ao processar mensagem: {e}")
        # ❗ Se não der ack, a mensagem será reenviada
        # Ou você pode usar dead-letter exchange se desejar

def callback(ch, method, properties, body):
    # Envia para execução paralela
    executor.submit(process_message, body, ch, method)

def start_worker():
    logger.info("Iniciando conexão com RabbitMQ...")
    credentials = pika.PlainCredentials(Config.RABBITMQ_USER, Config.RABBITMQ_PASSWORD)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=Config.RABBITMQ_HOST,
            credentials=credentials
        )
    )
    channel = connection.channel()

    # Garante que a fila seja durável
    channel.queue_declare(queue='produto_criado', durable=True)

    # Permite até 10 mensagens não confirmadas simultaneamente
    channel.basic_qos(prefetch_count=10)

    # Inicia o consumo
    channel.basic_consume(queue='produto_criado', on_message_callback=callback)

    logger.info("[*] Aguardando mensagens (até 10 simultaneamente). Pressione CTRL+C para sair.")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        logger.info("Encerrando consumo...")
        channel.stop_consuming()
    finally:
        connection.close()
        executor.shutdown(wait=True)

if __name__ == "__main__":
    start_worker()


# rodar com o comando:
# python3 -m app.workers.produto_worker