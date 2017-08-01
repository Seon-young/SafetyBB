import gps
import paho.mqtt.client as mqtt # MQTT Header

session = gps.gps("localhost", "2947") # Listen port 2947(gpsd)
session = gps.gps(mode=1)

client = mqtt.Client() # Create client

# Connect this client to broker
# (Broker's Host Name or IP Addr, Port Num, Live Time)
client.username_pw_set("root", "root")
client.connect("m10.cloudmqtt.com", 10290, 10)

def gpsf() :
    try :
            report = session.next()

            print "root/GPS/lat : ", report['lat']
            print "root/GPS/lon : ", report['lon']
            
            lat = report['lat']
            lon = report['lon']            

            # Publish msg to broker
            # (Topic, (string)Payload)
            client.publish("root/GPS/lat", lat)
            client.publish("root/GPS/lon", lon)

    except Exception as e:
        print 'GPS Check Error (Nothing)'
        print e


    

