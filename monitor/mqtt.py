import logging
import json
import paho.mqtt.client as mqtt

'''
Code to access my local MQTT broker at the given IP address
'''

class MqttMonitor:
    def __init__(self, IP_address, *, port=1883):
        self.IP_address = IP_address
        self.port = port
        self.client = mqtt.Client("")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, result):
        logging.debug("MqttMonitor: connected with result code %s", result)
        client.subscribe("clock") # so that we get at least one message per minute

    def on_message(self, client, userdata, msg):
        logging.debug("MqttMonitor: got message %s %s at %s", msg.topic, msg.payload, msg.timestamp)

    def on_disconnect(self, client, userdata, rc=0):
        logging.debug("MqttMonitor: Disconnected result code %s", rc)
        # self.client.loop_stop()

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def start(self):
        self.client.connect(self.IP_address, self.port) #establish connection
        self.client.loop_start() # spawn thread that calls loop() for us
