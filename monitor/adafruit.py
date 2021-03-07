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
        ##client.subscribe('pmacdougal/throttle') # feed from AdaFruit to subscribe to
        ## feeds from the loft
        #client.subscribe('s.lt')  # feed from AdaFruit
        ## feeds from the pumphouse
        #client.subscribe('s.ht')  # feed from AdaFruit
        #client.subscribe('s.it')  # feed from AdaFruit
        #client.subscribe('s.ot')  # feed from AdaFruit
        #client.subscribe('s.rt')  # feed from AdaFruit
        # feeds from the rpizw
        client.subscribe('s.mps')  # feed from AdaFruit

    def mqtt_disconnected(self, client):
        logging.info(
            'Adafruit.mqtt_disconnected(): io.adafruit.com MQTT broker disconnected.')

    def mqtt_message(self, client, topic, payload):
        logging.info(
            'Adafruit.mqtt_message(): got message %s with value %s.', topic, payload)
        # This is where all the work is done... parsing messages and deciding what to do with them
        if 's.mps' == topic:
            # forward to local broker
            self.local_broker.publish(topic, payload)
        elif ('s.ht' == topic
              or 's.it' == topic
              or 's.ot' == topic
              or 's.rt' == topic):
            # forward to local broker
            self.local_broker.publish(topic, payload)
        elif 's.lt' == topic:
            # forward to local broker
            self.local_broker.publish(topic, payload)

    def loop(self):
        # self.aio.loop_background is running
        pass
