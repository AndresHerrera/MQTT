import ssl
import sys

import paho.mqtt.client

def OnConnect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='home/kitchen/principal', qos=2)

def OnMessage(client, userdata, message):
    print('------------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %d' % message.qos)

def main():
    client = paho.mqtt.client.Client(client_id='client1', clean_session=False)
    client.on_connect = OnConnect
    client.on_message = OnMessage
    client.connect(host='127.0.0.1', port=1884)
    client.loop_forever()

if __name__ == '__main__':
    main()

sys.exit(0)
