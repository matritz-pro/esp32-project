from umqttsimple import MQTTClient
import time
import ubinascii
import machine

client_id = ubinascii.hexlify(machine.unique_id())
mqtt_server = '192.168.0.132'

# hold the last time a message was sent
last_message = 0
# time between each message sent
message_interval = 5
# counter to be added to the message
counter = 0

def connect_and_subscribe(topic_sub, callback):
    global client_id, mqtt_server
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(callback)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()


def start()
    while True:
    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
          msg = b'ping #%d' % counter
          client.publish(topic_pub, msg)
          last_message = time.time()
          counter += 1
    except OSError as e:
        restart_and_reconnect()

