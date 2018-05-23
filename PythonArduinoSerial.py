import serial
import time
import struct

arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(1)

# def parseData(con):
# 	dat = con.readline()
# 	dat = dat.decode('utf-8')
# 	dat = dat.replace('\r','')
# 	dat = dat.replace('\n', '')
# 	datArray = dat.split(' ')

# 	return datArray	

# def requestIrData(con):
# 	distArray = None
# 	con.write(b'1')
# 	time.sleep(0.1)
# 	if con.inWaiting() > 0:
# 		distArray = parseData(con)
# 		return distArray
# 	else:
# 		print('no data returned')

	

# def requestImuData(con):
# 	angleArray = None
# 	con.write(b'2')
# 	time.sleep(0.1)
# 	if con.inWaiting() > 0:
# 		angleArray = parseData(con)
# 	else:
# 		print('no data returned')

# 	return angleArray
mapArray = []

while arduino.is_open:
	try:
		IR = 1
		IMU = 2

		arduino.write(struct.pack('>B', IR))
		dat = arduino.readline()
		dat = dat.decode('utf-8')
		dat = dat.replace('\r','')
		dat = dat.replace('\n', '')
		dists = dat.split(' ')

		arduino.write(struct.pack('>B', IMU))
		dat = arduino.readline()
		dat = dat.decode('utf-8')
		dat = dat.replace('\r','')
		dat = dat.replace('\n', '')
		angles = dat.split(' ')

		if ('' not in angles) and ('' not in dists):
			print(dists)
			print(angles)
			for dist, angle in zip(dists, angles):
				p = (dist, angle)
				mapArray.append(p)

			print(mapArray)

	except Exception as e:
		raise e
		arduino.close()
		print("connection closed")

