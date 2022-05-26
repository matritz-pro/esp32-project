import mqtt

def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
        print('ESP received hello message')
        
try:
    client = mqtt.connect_and_subscribe(b'test', sub_cb)
except OSError as e:
    mqtt.restart_and_reconnect()

def start(topic):
    while True:
        try:
            client.check_msg()
            if (time.time() - last_message) > message_interval:
                msg = b'ping #%d' % counter
                client.publish(topic, msg)
                last_message = time.time()
                counter += 1
        except OSError as e:
            restart_and_reconnect()
