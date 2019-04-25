import json
import time

from kafka import KafkaProducer

class KafkaConnector(object):

    producer = None

    def __init__(self, **options):
        if not options.__contains__('bootstrap_servers'):
            raise KeyError("bootstrap_servers key is required")

        KafkaConnector.producer = KafkaProducer(**options)

    def send(self, data, topic):
        KafkaConnector.producer.send(topic, key=b'log', value=data)
