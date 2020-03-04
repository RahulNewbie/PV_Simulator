
import math
import pika
import numpy as np
import callback


def simulate(time_serialized):
    """
    Simulator function to make PV simulator
    """
    mu = 10
    variance = 2
    sigma = math.sqrt(variance)
    # pv simulation using numpy expression
    return np.exp(time_serialized - mu)**2 / (2 * sigma**2)


def start_receive_msg():
    """
    This method will consume the msgs from the rabbitmq
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # queue declaration
    channel.queue_declare(queue='meter', durable=True)
    channel.basic_consume(queue='meter',
                          on_message_callback=callback.callback_func)
    print('All messages are consumed.. Waiting for new messages')
    channel.start_consuming()


if __name__ == '__main__':
    # Start receiving msg from Rabbit MQ
    start_receive_msg()

