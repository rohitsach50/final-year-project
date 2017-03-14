import time
import serial
import httplib, urllib

#ser = serial.Serial('/dev/ttyUSB0',9600)
ser = serial.Serial('/dev/ttyACM0',9600)

a = []



data = ser.readline()





print "AUTO MATIC IRRIGATION SYSTEM"

while True:
	#ser = serial.Serial('/dev/ttyACM0',9600)
        data =  " " 
        data = ser.readline()
        a = data
        temp = " "
        hum = " "
        mois = " "
	print data
	intensity = " "
	temp = a[7]+a[8]+a[9]
	hum = a[18]+a[19]+a[20]
 	mois = a[29]+a[30]+a[31]
	intensity = a[40]+a[41]+a[42]
	print "temp"+temp+" deg C"
	print "humidity"+hum+"%"
	print "soil moisture"+mois+"%"
	print "sun intensity"+intensity+"%" 

	params = urllib.urlencode({'field1':temp,'field2':hum,'field3':mois,'field4':intensity,'key':'OLLKTR5P5JBU7EJS'})
	#params = urllib.urlencode({'field1':temp,'field2':hum,'field3':mois,'field4':intensity,'key':'EMHLK4TADMQ3I7IO'})
	#params = urllib.urlencode({'field1':122,'field2':23,'field3':45,'field4':98,'key':'EMHLK4TADMQ3I7IO'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data1  = response.read()
        conn.close()
	#time.sleep(5)
	
ser.close
print("serial port closed")
