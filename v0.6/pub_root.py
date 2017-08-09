import RPi.GPIO as gpio
import dht11
import paho.mqtt.client as mqtt # MQTT Header
import time # Hearder for 'sleep()'
import pub_root_gps
import calv

# initialize GPIO Temperature 
temperature = 0

# initialize GPIO Beltcheck
touchPin = 26 # D0 connected to D26
touchInvPin = 27 # A0 connected to D27
metal = 0

# Temperature
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.cleanup()

# Beltcheck
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.setup(touchPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# initialize GPIO Button
gpio.setup(18, gpio.IN,pull_up_down=gpio.PUD_UP)

def eventTouchSensor(e):
        if(e == 26) :
                global metal
                metal = 1

# read data using pin 5 Temperature
instance = dht11.DHT11(pin = 5)

client = mqtt.Client() # Create client

# Connect this client to broker
# (Broker's Host Name or IP Addr, Port Num, Live Time)
client.username_pw_set("root", "root")
client.connect("m10.cloudmqtt.com", 10290, 10)


# Beltcheck
gpio.add_event_detect(touchPin, gpio.RISING, bouncetime = 200, callback = eventTouchSensor)

velo = 0
lastlat = 0
lastlon = 0

try:
    while True:
        # Temperature
        result = instance.read()

        # Beltcheck
        global status

        # Button
        inputValue = gpio.input(18)

        # Button
        if (inputValue == False):
                print("root/Button : pressed")
                        
                # Publish msg to broker
                # (Topic, (string)Payload)
                client.publish("root/Button","on")

        global lastlat
        global lastlon
        global velo
        
        pub_root_gps.gpsf()


        if(pub_root_gps.lat != 0 and pub_root_gps.lon != 0 and lastlat != 0 and lastlon != 0) :
                velo = calv.v(lastlon, lastlat, pub_root_gps.lon, pub_root_gps.lat)/3600

        
        if(pub_root_gps.lat != 0 or pub_root_gps.lon != 0) :
                lastlat = pub_root_gps.lat
                lastlon = pub_root_gps.lon


	if(velo >= 0.0056) : # car
	
        # Beltcheck
        
                if(metal == 1): # metaltouch sensing is on
                    if(gpio.input(17) == 0) : # Breakbeam sensing is on
                        status = 3
                        client.publish("root/Beltcheck","on")
                        print("root/Beltcheck : on");
                                    
                    else:
                        status = 1
                        client.publish("root/Beltcheck","off")
                        print("root/Beltcheck : off");
                                    
                elif(metal == 0):
                                
                    if(gpio.input(17) == 0) : # Breakbeam sensing is on
                        status = 2
                                   
                    else:
                        client.publish("root/Beltcheck","off")
                        print("root/Beltcheck : off(2)");

                
	else : # nocar
                client.publish("root/Beltcheck","nocar")
                print("root/Beltcheck : nocar");

	

        # Temperature
        
        if result.is_valid():
                print("root/Temperature: %d C" % result.temperature)

                # Publish msg to broker
                # (Topic, (string)Payload)
                client.publish("root/Temperature", result.temperature)
                
        else:
                print("Temperature Check Error")
        


        time.sleep(1)
        
except KeyboardInterrupt: # if input 'Ctrl + C'
    print("pub_root End")
    gpio.cleanup()

    # Clean end to connect with broker
    client.disconnect()
