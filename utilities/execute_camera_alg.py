import sys, getopt
import os
import json
from datetime import datetime


try:
	opts, args = getopt.getopt(sys.argv[1:], "p:R:AB", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py MCSOA:B:Imsf")
	sys.exit()

A = 0
B = 0
for opt, arg in opts:
	if opt in ("-p", "--command"):
		Camera = arg
	if opt in ("-R", "--roomnum"):
		roomnum = int(arg)
	if opt in ("-A", "first cam"):
		A = 1
	if opt in ("-B", "second cam"):
		B = 1
Camera = Camera.replace('%', ' ')
print(Camera)
with open('./room_information.json') as f:
	temp = json.load(f)
count = 1
# for i in temp:
# 	for j in i['thermal']:
# 		# os.system('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
# 		os.system('mkdir ' + ('RP'+str(count)))
# 		count += 1
# 		# print('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
print(roomnum)
os.system(". /home/team19/Desktop/ENV/bin/activate")
if A == 0 and B == 0:
	if len(temp[roomnum-1]["camera"]) == 1:
		os.system(". /home/team19/Desktop/ENV/bin/activate|"+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + ' >running_stdout.txt&')
		# print(". /home/team19/Desktop/ENV/bin/activate | "+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + ' >running_stdout.txt&')
	else:
		os.system(". /home/team19/Desktop/ENV/bin/activate|"+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + " -b http://viewer:OPC-ECE-viewer@" + temp[roomnum-1]["camera"][1]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" +' >running_stdout.txt&')
		# print(". /home/team19/Desktop/ENV/bin/activate | "+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + ' >running_stdout.txt&')
elif A == 1 and B == 0:
	os.system(". /home/team19/Desktop/ENV/bin/activate|"+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + ' >running_stdout.txt&')
elif A == 0 and B == 1:
	os.system(". /home/team19/Desktop/ENV/bin/activate|"+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][1]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + ' >running_stdout.txt&')
elif A == 1 and B == 1:
	os.system(". /home/team19/Desktop/ENV/bin/activate|"+Camera + ' -a http://viewer:OPC-ECE-viewer@' + temp[roomnum-1]["camera"][0]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" + " -b http://viewer:OPC-ECE-viewer@" + temp[roomnum-1]["camera"][1]['cam_ip'] + "//axis-cgi/mjpg/video.cgi" +' >running_stdout.txt&')	

	

