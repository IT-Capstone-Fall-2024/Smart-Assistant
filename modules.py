import paho.mqtt.client as mqtt

broker = "10.42.0.1"
port = 1883
global topic, message
# username = 'emqx'
# password = 'public'


client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.connect(broker, 1883)
# client.publish(topic, "led", qos=1) # Testing connection

# Helper method for modules, compares list to module list and returns what is in the list
def compare(list, moduleList):
    selected = ""
    mSet = set(moduleList)
    for w in list:
        if w in mSet:
            selected = w
    return selected

# Light module 
def lights(list):
    global topic, message
    lightList = ["1", "2", "3", "4"] # can change to be however many options
    colorList = ["red", "orange", "blue", "purple", "yellow", "green", "white"]
    stateList = ["on", "off"]
    color = compare(list, lightList)
    number = compare(list, colorList)
    state = compare(list, stateList)
    topic = "light" + number
    message = state + color
    client.publish(topic, message, qos=1)

# Lock module
def lock(list):
    global topic, message
    doorList = ["front", "back"]
    stateList = ["lock", "unlock"]
    door = compare(list, doorList)
    state = compare(list, stateList)
    topic = door + "door"
    message = state 
    client.publish(topic, message, qos=1)

