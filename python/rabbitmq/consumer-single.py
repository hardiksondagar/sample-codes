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

    while True:
        method_frame, header_frame, body = channel.basic_get(queue_name)
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
            print("Consumed:", body)
