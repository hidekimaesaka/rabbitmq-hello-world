from app import start_producer


def produce_message(msg=None):

    if not msg: msg = 'Ooops, there is no message'

    start_producer(msg)


if __name__ == '__main__':

    try:
        produce_message('lucas')

    except Exception as e:
        print(e)
