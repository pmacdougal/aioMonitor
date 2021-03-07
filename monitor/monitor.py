# This script monitors topics in io.adafruit.com and publishes some of them to my local MQTT broker
import logging
import time
import sys
from .mqtt import MqttMonitor
from .handler import Generic, GenericEnergy, GenericString
from .adafruit import Adafruit
from .private import username, password
# private.py is not part of the checked in code.  You will need to create it.
# It is a two line file with your Adafruit IO username and access key in it:
#     username = 'xxxxxxxx'
#     password = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

class Monitor:
    def __init__(self):
        pass

    def configure(self, mqtt_monitor, metering_queue):
        # must be overridden
        raise NotImplementedError

    def run(self, msg, topic, mqtt_ip):

        try:
            mqtt_monitor = MqttMonitor(mqtt_ip)
            aio = Adafruit(username, password, mqtt_monitor)
            mqtt_monitor.start()
            while True:
                try:
                    aio.loop()
                except Exception as e:
                    logging.error('Exception: %s', e)

        except Exception as e:
            logging.error('Exception: %s', e)
            status = 1
        except KeyboardInterrupt:
            status = 2
        #except NotImplementedError:
        #    don't catch this exception
        else:
            status = 0 # if normal exit
        finally:
            # all exits
            sys.stdout.flush()
            sys.stderr.flush()
            return(status)

