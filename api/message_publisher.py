import logging
import os
from kombu import Exchange, Producer, Connection

logger = logging.getLogger(__name__)


def publish_message(body, routing_key):
    try:
        with Connection(os.environ['MESSAGE_BROKER_URL']) as conn:
            with conn.channel() as channel:
                exchange = Exchange(os.environ['MESSAGE_BROKER_EXCHANGE'],
                                    type='topic', channel=channel, durable=True)
                exchange.declare()
                producer = Producer(channel=channel,
                                    exchange=exchange,
                                    routing_key=routing_key,
                                    serializer='json')
                producer.publish(body=body, retry=True)
    except Exception as ex:
        # TODO: Handle this better
        logging.error(f"Something went wrong in publish_message - {ex.__class__} - {ex}")
