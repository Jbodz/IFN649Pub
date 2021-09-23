import serial
import time
import string
import paho.mqtt.publish as publish

#communications
ser=serial.Serial("/dev/rfcomm2",9600) #teensy1
ser.write(str.encode('Start\r\n'))

while True:
    if ser.in_waiting>0:
        rawserial=ser.readline()
        cookedserial=rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
#splitting       
        split1=cookedserial.split(" ") #to split using space as deliminter
        soilValue=split1[3]
        lightValue=split1[7]
        humidValue=split1[9][:-1]
        tempValue=split1[12][:-1]
        print(soilValue)
        print(lightValue)
        print(humidValue)
        print(tempValue)

#to publish      
        msgs=[{'topic':"topicLightValue", 'payload':lightValue},
              ("topicHumidValue", humidValue),
              ("topicSoilValue", soilValue),
              ("topicTempValue", tempValue)]
        publish.multiple(msgs, hostname="localhost")
        print("Published")
