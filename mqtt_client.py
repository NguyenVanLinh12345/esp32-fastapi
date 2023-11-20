import time
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "probe_122/912658279992300_probe_122"
username = 'backend_iot'
password = '1234'
client_id = 'client_test'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    client.username_pw_set(username=username, password=password)
    client.connect(broker, port)
    client.on_connect = on_connect
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.publish(topic, "xin chao")
    client.publish("may_1/esp32", "xin chao esp32, day la python")
    client.on_message = on_message

if __name__ == "__main__":
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()