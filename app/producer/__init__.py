import pika

conn_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(conn_params)

def run():

    try:
        channel = connection.channel()

    except Exception as e:
        print(e)

    return channel


def create_queue(channel, queue_name):

    try:
        channel.queue_declare(queue=queue_name)

    except Exception as e:
        print(e)

    return channel

def close_connection():

    try:
        connection.close()
        return True

    except Exception as e:
        print(e)

    return False
