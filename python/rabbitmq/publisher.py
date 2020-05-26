import pika

queue_name = 'your-queue-name'


def get_channel():
    parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return channel


if __name__ == '__main__':

    channel = get_channel()
    queue_name = queue_name

    for i in range(5):
        message = 'message#{index}'.format(index=i+1)
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print("Published:", message)
