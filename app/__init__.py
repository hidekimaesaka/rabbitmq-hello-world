from app import producer
from app import consumer


def start_producer(msg):

    channel = producer.run()

    producer.create_queue(channel, 'hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=msg)


def start_consumer() -> None:

    consumer.run('hello')
