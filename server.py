
import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('13.214.169.24')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


def on_reply_message_received(ch, method, properties, body):
    print(f"Request recieved: {properties.correlation_id}")
    ch.basic_publish(exchange='', routing_key=properties.reply_to,
    body=f"Hey its your reply to {properties.correlation_id}")


channel.queue_declare(queue="request-queue")
channel.basic_consume(
    queue="request-queue",
    auto_ack=True,
    on_message_callback=on_reply_message_received)

print("Start Server")

channel.start_consuming()



