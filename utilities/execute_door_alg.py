import sys, getopt
import os
import json
from datetime import datetime


try:
	opts, args = getopt.getopt(sys.argv[1:], "p:R:r:d:", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py MCSOA:B:Imsf")
	sys.exit()

rate = ""
tempsave = ""
temperature = "python3 ./rpi-realtime-peoplecount/temp_monitor/collect_temp_info.py "
for opt, arg in opts:
	if opt in ("-p", "--command"):
		RP = arg
	if opt in ("-R", "--roomnum"):
		roomnum = int(arg)
	if opt in ("-r", "--rate"):
		temperature = temperature + " -r " + arg
	if opt in ("-d", "--tempsave"):
		temperature = temperature + " -d " + arg
RP = RP.replace('_', ' ')
# print(RP)
with open('/home/team19/COSSY/room_information.json') as f:
	temp = json.load(f)
count = 1
for i in temp:
	for j in i['thermal']:
		# os.system('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
		os.system('mkdir ' + ('RP'+str(count)))
		count += 1
		# print('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
# print(roomnum)
for i in temp[roomnum-1]['thermal']:
	# print(temperature)
	os.system('ssh ' + i['thermal_ip'] + ' ' + RP + '&')
	os.system('ssh ' + i['thermal_ip'] + ' ' + temperature + '&')
	# print(i)
	# print('ssh ' + i['thermal_ip'] + ' ' + RP + '&')



