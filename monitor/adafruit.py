import logging
import time
import datetime
from Adafruit_IO import MQTTClient

'''
ToDo:
'''


class Adafruit:
    def __init__(self, username, password, local_broker):
        logging.info('Adafruit.__init__(): Connecting to io.adafruit.com ...')
        self.aio = MQTTClient(username, password, secure=False)
        self.aio.on_connect = self.mqtt_connected
        self.aio.on_disconnect = self.mqtt_disconnected
        self.aio.on_message = self.mqtt_message
        self.local_broker = local_broker
        try:
            self.aio.connect()
        except TimeoutError:
            logging.info('Adafruit.__init__(): Connection timed out')
        else:
            self.aio.loop_background()

    def mqtt_connected(self, client):
        logging.info(
            'Adafruit.mqtt_connected(): io.adafruit.com MQTT broker connected.')
        #client.subscribe('pmacdougal/throttle') # feed from AdaFruit to subscribe to
        #client.subscribe('#') # all feeds
        client.subscribe('rriba.b0')
        client.subscribe('rriba.duration')
        client.subscribe('s.ht')
        client.subscribe('s.it')
        client.subscribe('s.lt')
        client.subscribe('s.mph')
        client.subscribe('s.ot')
        client.subscribe('s.rt')
        client.subscribe('s.sq')
        client.subscribe('s.ups')
        

    def mqtt_disconnected(self, client):
        logging.info(
            'Adafruit.mqtt_disconnected(): io.adafruit.com MQTT broker disconnected.')

    def mqtt_message(self, client, topic, payload):
        logging.info(
            'Adafruit.mqtt_message(): got message %s with value %s.', topic, payload)
        # This is where all the work is done... parsing messages and deciding what to do with them
        if topic.startswith('h.'):
            # home data
            pass
        elif topic.startswith('g.'):
            # garage data
            pass
        elif topic.startswith('rriba.'):
            # forward to local broker
            self.local_broker.publish(topic, payload)
        elif topic.startswith('s.'):
            # forward to local broker
            self.local_broker.publish(topic, payload)

    def loop(self):
        # self.aio.loop_background is running
        pass
