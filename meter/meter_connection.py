def connect_to_rabbit_mq(conn):
    """
    Connect to the broker and return the channel
    """
    channel = conn.channel()
    channel.queue_declare(queue='meter', durable=True)
    return channel