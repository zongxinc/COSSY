# Based on u3allio.c

import sys
from datetime import datetime
import time
import u3

quickSample = 1
longSettling = 0
numIterations = 1000
numChannels = 1

max_num_people = 50
curr_num_people = int(sys.argv[1])
#print('Current Number of People= ', curr_num_people)
final_digital = round((curr_num_people/max_num_people)*(2**16))
#print('Digital Value Calculated= ', final_digital)
expected_vol = (curr_num_people/max_num_people)*(5)
#print('Expected Voltage= ', expected_vol)

d = u3.U3()
d.getCalibrationData()
FIOEIOAnalog = (2 ** numChannels) - 1
fios = FIOEIOAnalog & 0xFF
eios = FIOEIOAnalog // 256
d.configIO(FIOAnalog=fios, EIOAnalog=eios)

d.getFeedback(u3.PortDirWrite(Direction=[0, 0, 0], WriteMask=[0, 0, 15]))

feedbackArguments = []
feedbackArguments.append(u3.DAC1_16(Value = final_digital))

if d.configU3()['VersionInfo'] & 18 == 18:
    isHV = True
else:
    isHV = False

results = d.getFeedback(feedbackArguments)

