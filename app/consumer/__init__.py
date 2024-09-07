import pika

conn_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(conn_params)


def run(queue):

    try:
        channel = connection.channel()
        channel.queue_declare(queue=queue)

        def callback(ch, method, properties, body):
            print(f" [x] Received {body}")

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    except Exception as e:
        print(e)
