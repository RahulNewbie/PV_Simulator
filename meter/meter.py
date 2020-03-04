import json
import pika
from datetime import datetime, timedelta
import random
import meter_connection


def generate_msg(datetime_data, seconds):
    """
    This method generate random power value upto 3 decimal digits
    and timestamp.

    """
    return {
        'timestamp': datetime.timestamp(datetime_data +
                                        timedelta(seconds=seconds*2)),
        'power_value': round(random.uniform(0, 9000), 3)
    }


def publish_to_broker(channel, msg):
    """
    publish the msgs using broker
    """
    msg_body = json.dumps(msg)
    channel.basic_publish(exchange='', routing_key='meter', body=msg_body,
                          properties=pika.BasicProperties(delivery_mode=2,))
    print("Sent_msg {0}".format(msg_body))


def start_sending_pv_data():
    """
    Responsible for connecting broker and send msgs in the queue
    """
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        # Connect the rabbit mq
        channel = meter_connection.connect_to_rabbit_mq(connection)
        # Get date time
        datetime_data = datetime.now().replace(microsecond=0)
        for seconds in range(24 * 60 * 30):
            # Publish to broker with msgs
            publish_to_broker(channel, generate_msg(datetime_data, seconds))


if __name__ == '__main__':
    # Start receiving msg from Rabbit MQ
    start_sending_pv_data()

