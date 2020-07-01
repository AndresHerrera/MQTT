import paho.mqtt.client as mqtt

#Publisher
client = mqtt.Client()
client.connect("localhost",1884,60)
client.publish("home/kitchen/principal", "{temp:12, status:'off'}");
client.disconnect();