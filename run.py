import transcribe
import modules
import os
import whisper
import paho.mqtt.client as mqtt

# MQTT Variables
broker = "192.168.90.234"
port = 1883
confirmTopic = "assist/confirm"
subTopic = "assist/listen"

# Connects MQTT Client
client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.connect(broker, port)

# Global Variables
global module

# Loading STT Model
model = whisper.load_model("tiny") # best for use with RPi


# Runs function from transcribe.py to get query
def get_query(message):
    print("Transcribing")
    query = transcribe.linux_transcribe(model)
    return query

# Splits and Identifies the module from the query
def splitAndID(query):
    global module
    splitList = query.split()
    if ("light" in splitList) or ("lights" in splitList) or ("like" in splitList) or ("likes" in splitList):
        modules.lights(splitList)
    if ("door" in splitList) or ("lock" in splitList):
        modules.lock(splitList)
    if ("camera" in splitList) or ("scan" in splitList):
        modules.camera(splitList)

# Runs when MQTT recieves a mesage from subscribed topic
# Checks if activator message was correct, then runs the transcribe method
def on_message(client, userdata, message):
    decoded_message = str(message.payload.decode("utf-8"))
    client.publish(confirmTopic, "Got Message: " + decoded_message)
    print("Got Message: " + decoded_message)
    if (decoded_message == "voice"):
        client.publish(confirmTopic, "Transcribing")
        query = get_query(message)
        splitAndID(query)

# Main Method
def main():
    print("Running")
    # Sets to run function when recieving a message
    client.on_message = on_message

    # Publishes to confirmation topic to tell it started
    client.publish(confirmTopic, "Listening")

    # Subscribes to listener for activator message
    client.subscribe(subTopic)

    # Loops forever as a daemon
    client.loop_forever()

if __name__ == '__main__':
    main()
