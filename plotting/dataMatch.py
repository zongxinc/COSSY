import os
import json
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dateutil.relativedelta
import sys, getopt


try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py -N <reportTime>")
	sys.exit()
for opt, arg in opts:
	if opt == "-h":
		print("-f, result folder name")
		sys.exit()
	elif opt in ("-f", "output"):
		resultfolder = str(arg)

files = sorted(os.listdir('/home/team19/COSSY/' + resultfolder))
ts_folder = resultfolder.replace('room2_', '')
print(ts_folder)

jsonList = []
for file in files:
	if '.json' in file:
		if not '._' in file:
			jsonList.append(file)
jsonList = sorted(jsonList)
fusion_ts = []
fusion_count = []
print(jsonList[0][:-5])
dt1 = datetime.datetime.fromtimestamp(float(jsonList[0][0:len(jsonList[0])-5]))
for i in range(len(jsonList)):
	dt2 = datetime.datetime.fromtimestamp(float(jsonList[i][0:len(jsonList[i])-5]))
	diff = dateutil.relativedelta.relativedelta(dt2, dt1)
	sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
	fusion_ts.append(sec)
	with open('/home/team19/COSSY/' + resultfolder + jsonList[i]) as f:
		temp = json.load(f)
		# print(type(temp[jsonList[i][0:len(jsonList[i])-5]]))
		fusion_count.append(temp[jsonList[i][0:len(jsonList[i])-5]][0])

Camerafoldername = ['/home/team19/Desktop/Axis_DL/Detection/YOLO/' + ts_folder + 'Camera 1/', '/home/team19/Desktop/Axis_DL/Detection/YOLO/' + ts_folder + 'Camera 2/', '/home/team19/Desktop/Axis_DL/Detection/YOLO/' + ts_folder + 'Camera 3/']
cam_intermediate_count = np.zeros(len(Camerafoldername))
camdict = []
camLast = 0
for i in range(len(Camerafoldername)):
	camdict.append({})
ts_temp = []
NUC_ts = []
NUC_count = np.array([])
for i in range(len(Camerafoldername)):
	files = sorted(os.listdir(Camerafoldername[i]))
	jsonList = []
	for file in files:
		if '.json' in file:
			if not '._' in file:
				jsonList.append(file)
	camEnd = len(jsonList)
	for j in range(camLast, camEnd):
		ts_temp.append(float(jsonList[j][0:len(jsonList[j])-5]))
		# print("append", float(jsonList[j][0:len(jsonList[j])-5]))
		with open(Camerafoldername[i] + jsonList[j]) as f:
			temp = json.load(f)
			camdict[i][float(jsonList[j][0:len(jsonList[j])-5])] = temp["Num People"]

ts_temp.sort()
if len(ts_temp) != 0:
	NUC_ts = NUC_ts + ts_temp
# print("cam_ts len", cam_ts)
#after sorting the cam_ts, append each count to the cam_count in the order of cam_ts
for i in range(len(ts_temp)):
	cam_intermediate_count = np.zeros(len(Camerafoldername)) 
	for j in range(len(Camerafoldername)):
		if ts_temp[i] in camdict[j]:	
			cam_intermediate_count[j] = camdict[j][ts_temp[i]]
			print(cam_intermediate_count[j], ts_temp[i])
	NUC_count = np.append(NUC_count, sum(cam_intermediate_count))

fusion_count_g = []
fusion_ts_g = []
for i in range(len(fusion_ts)):
	# dt2 = datetime.datetime.fromtimestamp(fusion_ts[i])
	# diff = dateutil.relativedelta.relativedelta(dt2, dt1)
	# sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
	if i !=0:
		fusion_ts_g.append(fusion_ts[i])
		fusion_count_g.append(fusion_count[i-1])
	else:
		fusion_ts_g.append(fusion_ts[i])
		fusion_count_g.append(0)
	fusion_ts_g.append(fusion_ts[i])
	fusion_count_g.append(fusion_count[i])
print(fusion_count_g)
print(fusion_ts_g)
NUC_count_g = []
NUC_ts_g = []
for i in range(len(NUC_ts)):
        dt2 = datetime.datetime.fromtimestamp(fusion_ts[i])
        diff = dateutil.relativedelta.relativedelta(dt2, dt1)
        print(dt1)
        print(dt2)
        sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
        if i !=0:
                NUC_ts_g.append(sec)
                NUC_count_g.append(NUC_count[i-1])
        else:
                NUC_ts_g.append(sec)
                NUC_count_g.append(0)
        NUC_ts_g.append(sec)
        NUC_count_g.append(NUC_count[i])
print(NUC_ts_g)
print(NUC_count_g)

RPfoldername = ["/home/team19/COSSY/RP1", "/home/team19/COSSY/RP2"]
RP_ts = []
RP_dict = []
RP1_ts = []
RP2_ts = []
RP1_count = []
RP2_count = []
count = np.zeros(len(RPfoldername))
for i in range(len(RPfoldername)):
	RP_dict.append({})

for i in range(len(RPfoldername)):
	myfiles = np.array(os.listdir(RPfoldername[i]))
	myfiles.sort()
	for j in range(len(myfiles)):
		if "._" not in myfiles[j]:
			with open(RPfoldername[i] + "/" + myfiles[j], encoding='utf-8') as f:
				temp = json.load(f)
				# print(RPfoldername[i] + "/" + myfiles[j])
				RP_ts.append(float(temp['timestamp']))
				# print(float(temp['timestamp']), int(temp['count']))
				if i == 0:
					RP_dict[i][float(temp['timestamp'])] = int(temp['count'])
				else:
					RP_dict[i][float(temp['timestamp'])] = int(temp['count'])
				if i == 0:
					dt2 = datetime.datetime.fromtimestamp(float(temp['timestamp']))
					diff = dateutil.relativedelta.relativedelta(dt2, dt1)
					sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
					RP1_ts.append(sec)
					RP1_count.append(int(temp['count']))
				else:
					dt2 = datetime.datetime.fromtimestamp(float(temp['timestamp']))
					diff = dateutil.relativedelta.relativedelta(dt2, dt1)
					sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
					RP2_ts.append(sec)
					RP2_count.append(int(temp['count']))
# print(RP1_count)
# print(RP2_count)
RP_ts.sort()
RP_count = []

for i in range(len(RP_ts)):
	for j in range(len(RPfoldername)):
		if RP_ts[i] in RP_dict[j]:
			count[j] = RP_dict[j][RP_ts[i]]
	RP_count.append(sum(count))
# print(RP_count)
RP_ts_g = []
RP_count_g = []
RP_ts_g.append(0)
RP_count_g.append(0)
for i in range(len(RP_ts)):
	dt2 = datetime.datetime.fromtimestamp(RP_ts[i])
	diff = dateutil.relativedelta.relativedelta(dt2, dt1)
	sec = diff.days* 86400 + diff.hours * 3600 + diff.minutes * 60 + diff.seconds
	# print(sec)
	if i !=0:
		RP_ts_g.append(sec)
		RP_count_g.append(RP_count[i-1])
	else:
		RP_ts_g.append(sec)
		RP_count_g.append(0)
	RP_ts_g.append(sec)
	RP_count_g.append(RP_count[i])
RP_ts_g.append(NUC_ts[-1])
RP_count_g.append(RP_count[-1])

RP1_ts_g = []
RP1_count_g = []
RP1_ts_g.append(0)
RP1_count_g.append(0)
for i in range(len(RP1_ts)):
	if i !=0:
		RP1_ts_g.append(RP1_ts[i])
		RP1_count_g.append(RP1_count[i-1])
	else:
		RP1_ts_g.append(RP1_ts[i])
		RP1_count_g.append(0)
	RP1_ts_g.append(RP1_ts[i])
	RP1_count_g.append(RP1_count[i])
RP1_ts_g.append(NUC_ts[-1])
RP1_count_g.append(RP1_count[-1])

RP2_ts_g = []
RP2_count_g = []
RP2_ts_g.append(0)
RP2_count_g.append(0)
for i in range(len(RP2_ts)):
	if i !=0:
		RP2_ts_g.append(RP2_ts[i])
		RP2_count_g.append(RP2_count[i-1])
	else:
		RP2_ts_g.append(RP2_ts[i])
		RP2_count_g.append(0)
	RP2_ts_g.append(RP2_ts[i])
	RP2_count_g.append(RP2_count[i])
RP2_ts_g.append(NUC_ts[-1])
RP2_count_g.append(RP2_count[-1])

# print(NUC_count)
# print(fusion_count)
# plt.figure()
# plt.plot(NUC_ts, NUC_count, "b", label="NUC")
# plt.savefig("Fusion_NUC.png")
NUC_ts = np.array(NUC_ts)
fusion_ts = np.array(fusion_ts)

print(RP1_ts_g)
print(RP1_count_g)
print(RP2_ts_g)
print(RP2_count_g)

with open('test.npy', 'wb') as f:
	np.save(f, NUC_ts)
	np.save(f, fusion_ts)
	np.save(f, NUC_count)
	np.save(f, fusion_count)
print(len(NUC_count))
plt.figure()
plt.plot([t/60 for t in NUC_ts], [float(count) for count in NUC_count], "b", label="OFC")
plt.plot([t/60 for t in fusion_ts_g], [float(count) for count in fusion_count_g], "r", label="Fusion")
# plt.xlim([0, 50])
plt.yticks(np.arange(-5, 8, 1.0))
plt.title("Fusion and OFC")
plt.xlabel("Time (minutes)")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("Fusion_OFC_count.png")


plt.figure()
fig,ax = plt.subplots()
l1, = ax.plot([t/60 for t in fusion_ts_g], [float(count) for count in fusion_count_g], "r", label="Fusion")
# plt.xlim([0, 50])
# plt.ylim([-10, 10])
ax.set_yticks(np.arange(-5, 10, 1), minor=False)
ax.set_ylabel("Number of people(Fusion)", color="red")
ax.set_xlabel("Time (minutes)")
ax2 = ax.twinx()
l2, = ax2.plot([t/60 for t in RP_ts_g], [float(count - 0.1) for count in RP_count_g], 'g', label="TDS toal")
# plt.xlim([0, 50])
# plt.ylim([-10, 10])
# print([float(count) for count in RP_count_g])
plt.title("Fusion and TDS total")
ax2.set_xlabel("Time (minutes)")
ax2.set_yticks(np.arange(-5, 10, 1.0), minor=False)
ax2.set_ylabel("Number of people(TDS total)", color='green')
# ax.legend()
# ax2.legend()
plt.legend([l1, l2], ["Fusion", "TDS total"])
plt.savefig("Fusion_TDS_count.png")

plt.figure()
fig,ax = plt.subplots()
l1, = ax.plot([t/60 for t in NUC_ts], [float(count) for count in NUC_count], "r", label="OFC")
# plt.xlim([0, 50])
# plt.ylim([-10, 10])
ax.set_yticks(np.arange(-5, 10, 1), minor=False)
ax.set_ylabel("Number of people(OFC)", color="blue")
ax.set_xlabel("Time (minutes)")
ax2 = ax.twinx()
l2, = ax2.plot([t/60 for t in RP_ts_g], [float(count - 0.1) for count in RP_count_g], 'g', label="TDS toal")
# plt.xlim([0, 50])
# plt.ylim([-10, 10])
# print([float(count) for count in RP_count_g])
plt.title("OFC and TDS total")
ax2.set_xlabel("Time (minutes)")
ax2.set_yticks(np.arange(-5, 10, 1), minor=False)
ax2.set_ylabel("Number of people(TDS total)", color='green')
# ax.legend()
# ax2.legend()
plt.legend([l1, l2], ["OFC", "TDS total"])
plt.savefig("OFC_TDS_count.png")

plt.figure()
plt.plot([t/60 for t in RP1_ts_g], [float(count) for count in RP1_count_g], "r", label="TDS1 10.241.10.33")
plt.plot([t/60 for t in RP2_ts_g], [float(count) for count in RP2_count_g], "b", label="TDS2 10.241.10.32")
# plt.xlim([0, 50])
plt.yticks(np.arange(-5, 8, 1.0))
# plt.ylim([-10, 10])
plt.title("TDS1 and TDS2")
plt.xlabel("Time (minutes)")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("TDS1_TDS2_count.png")

print(fusion_ts[-1])
print(NUC_ts[-1])






