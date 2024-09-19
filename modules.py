import paho.mqtt.client as mqtt

broker = "10.42.0.1"
port = 1883
topic = "testTopic"
# username = 'emqx'
# password = 'public'


client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.connect(broker, 1883)
client.publish(topic, "led", qos=1)