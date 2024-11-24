import paho.mqtt.client as mqtt

broker = "192.168.90.234"
port = 1883
global topic, message


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

def numberFix(number):
    if number == "one":
        return "1"
    if number == "two":
        return "2"
    if number == "three":
        return "3"
    if number == "four":
        return "4"
    return number

# Light module
def lights(list):
    global topic, message
    lightList = ["one", "1", "two", "2", "three", "3", "four", "4"] # can change to be however many options
    colorList = ["red", "orange", "blue", "purple", "yellow", "green", "white"]
    stateList = ["on", "off"]
    color = compare(list, colorList)
    number = compare(list, lightList)
    state = compare(list, stateList)
    number = numberFix(number)
    topic = "light/" + number
    # Debug
    print("Color: " + color + " Number: " + number + " State: " + state)
    message = state + " " + color
    print("Topic: " + topic + " Message: " + message)
    client.publish(topic, message, qos=1)

# Lock module
def lock(list):
    global topic, message
    doorList = ["one", "1", "two", "2", "three", "3", "four", "4"]
    stateList = ["lock", "unlock"]
    door = compare(list, doorList)
    door = numberFix(door)
    state = compare(list, stateList)
    topic =  "lock/" + door
    message = state
    # Debug
    print("Topic: " + topic + " Message: " + message)
    client.publish(topic, message, qos=1)

# Camera module
def camera(list):
    global topic, message
    cameraList = ["one", "1", "two", "2"]
    camera = compare(list, cameraList)
    camera = numberFix(camera)
    topic = "camera/" + camera
    message = "camera"
    client.publish(topic, message, qos=1)
