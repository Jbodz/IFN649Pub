import serial
import string
import paho.mqtt.client as mqtt #import the client
import time

ser=serial.Serial("/dev/rfcomm3",9600)
ser.write(str.encode('Start\r\n'))

def on_connect(client, userdata, flags, rc): # func for making connection
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    #client.subscribe("topicLightValue") #single sub
    client.subscribe([("topicLightValue", 0),("topicHumidValue", 0),("topicTempValue", 0),("topicSoilValue", 0)])#multiple subs
        
def on_message(client, userdata, msg): # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
    if(str(msg.topic)=='topicLightValue'):
        if(float(msg.payload)>50):
            ser.write(str.encode('lightHigh\r\n'))
        else:
            ser.write(str.encode('lightLow\r\n'))
    elif(str(msg.topic)=='topicSoilValue'):
        if(float(msg.payload)>30):
            ser.write(str.encode('soilHigh\r\n'))
        else:
            ser.write(str.encode('soilLow\r\n'))
    
    #if(str(msg.topic)=='topicHumidValue'):
    #    if(float(msg.payload)>25):
    #        ser.write(str.encode('humidHigh\r\n'))
    #    else:
    #        ser.write(str.encode('humidLow\r\n'))
    
    #if(str(msg.topic)=='topicTempValue'):
    #    if(float(msg.payload)>25):
    #        ser.write(str.encode('tempHigh\r\n'))
    #    else:
    #        ser.write(str.encode('tempLow\r\n'))
    
    #if(str(msg.topic)=='topicSoilValue'):
    #    if(float(msg.payload)>30):
    #        ser.write(str.encode('soilHigh\r\n'))
    #    else:
    #        ser.write(str.encode('soilLow\r\n'))
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
