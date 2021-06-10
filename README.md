### BOSTON UNIVERSITY
### COSSY - Computational Occupancy Sensing System  


## Setting up COSSY in a new deployment.

# You must have IP addresses for all devices (an IP address for each MAC address).
# Then, run:

cd cossy
python3 COSSY-setup.py

# Answer all questions. Door sensor and camera IDs are printed on each device.
# Make sure all the answers are correct so that the system can connect to all devices.


## Starting COSSY

# Make sure that no one stands under door sensors for the first 10 sec of system operation.
# Run:

cd cossy
bash COSSY-start.sh [flags]

# Flags:

  "-R N" run COSSY in room number 1 (N=1) or 2 (N=2); to run in 2 rooms, run the script twice
  "-O"   save all results (cameras, door sensors, fusion) in directory with time-stamped name; otherwise, default directory ### BOSTON UNIVERSITY
### COSSY - Computational Occupancy Sensing System  


## Setting up COSSY in a new deployment.

# You must have IP addresses for all devices (an IP address for each MAC address).
# Then, run:

cd cossy
python3 COSSY-setup.py

# Answer all questions. Door sensor and camera IDs are printed on each device.
# Make sure all the answers are correct so that the system can connect to all devices.


## Starting COSSY

# Make sure that no one stands under door sensors for the first 10 sec of system operation.
# Run:

cd cossy
bash COSSY-start.sh [flags]

# Flags:

  "-R N" run COSSY in room number 1 (N=1) or 2 (N=2); to run in 2 rooms, run the script twice
  "-O"   save all results (cameras, door sensors, fusion) in directory with time-stamped name; otherwise, default directory 
  "-S"   save images captured by the camera(s); default: images not saved
  "-s"   save thermal frames captured by door sensor(s); default: thermal frames not saved
  "-m"   use the multi-people algorithm in door sensors; default: single-people algorithm
  "-D"   use the DAC to convert the fusion result to voltage; default: DAC not used
  "-C N" use camera N only, (N=1 for camera 1 or N=2 for camera 2)
  "-r N" save R-Pi temperature every N seconds; if N=0 no recording of temperature; efault: N= 60 [sec]; 

# Example: run COSSY in room #1:

bash COSSY-start.sh -O -R 1 &

# Example: run COSSY in room #2 and save thermal frames:

bash COSSY-start.sh -O -R 2 -s &


## Stopping COSSY

# First, hit "Enter" on the keyboard (to get the prompt) and then:

bash COSSY-stop.sh [flags]

# Flags:

  "-R N" stop COSSY in room number 1 (N=1) or 2 (N=2); to stop in 2 rooms, run the script twice

# Example: stop COSSY running in room 1:

bash COSSY-stop.sh -R 1


## Ploting the results

# Go to the "plotting" folder and run:

python3 dataMatch.py -f [result folder name]

# Remember to add `/` at the end of folder name, like below:

python3 dataMatch.py -f 05-11-2021-03:04:47/


## Locations of relevenat source relevant code:

# Cameras:

# Room 1: /home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy.py
# Room 2: /home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy_room2.py

# Camera results: /home/team19/Desktop/Axis_DL/Detection/YOLO/{time_stamped folder name}

# Fusion:

# Room 1: /home/team19/COSSY/utilities/execute_fusion_alg.py 
# Room 2: /home/team19/COSSY/utilities/execute_fusion_alg_room2.py

# Fusion results: /home/team19/COSSY/{time_stamped folder name}
# RP Sync results: /home/team19/COSSY/{RP1 or RP2 or RP3 or RP4}

# Plotting:

# /home/team19/COSSY/plotting/COSSY_plotting.py


## Notes:

# The output from the RAPID wrapper is redirected to file "running_stdout.txt" located in
# the wrapper's directory so that the stream of messages does not overwhelm the screen.

# The output from Rsync, that synchronizes door-sensor files with the NUC, is redirected to file
# "autoSync.txt" located in the current directory.

# JSON files from the door sensors are located in directories named "RP#"

# People-counting results are stored in directories with time-stamped names

  "-S"   save images captured by the camera(s); default: images not saved
  "-s"   save thermal frames captured by door sensor(s); default: thermal frames not saved
  "-m"   use the multi-people algorithm in door sensors; default: single-people algorithm
  "-D"   use the DAC to convert the fusion result to voltage; default: DAC not used
  "-C N" use camera N only, (N=1 for camera 1 or N=2 for camera 2)
  "-t N" save R-Pi temperature every N minutes; if N=0 no recording of temperature; efault: N= 1 [min]; 

# Example: run COSSY in room #1:

bash COSSY-start.sh -O -R 1 &

# Example: run COSSY in room #2 and save thermal frames:

bash COSSY-start.sh -O -R 2 -s &


## Stopping COSSY

# First, hit "Enter" on the keyboard (to get the prompt) and then:

bash COSSY-stop.sh [flags]

# Flags:

  "-R N" stop COSSY in room number 1 (N=1) or 2 (N=2); to stop in 2 rooms, run the script twice

# Example: stop COSSY running in room 1:

bash COSSY-stop.sh -R 1


## Ploting the results

# Go to the "plotting" folder and run:

python3 COSSY_plotting.py -f [result folder name]

# Remember to add `/` at the end of folder name, like below:

python3 COSSY_plotting.py -f 05-11-2021-03:04:47/


## Locations of relevenat source relevant code:

# Cameras:

# Room 1: /home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy.py
# Room 2: /home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy_room2.py

# Camera results: /home/team19/Desktop/Axis_DL/Detection/YOLO/{time_stamped folder name}

# Fusion:

# Room 1: /home/team19/COSSY/utilities/execute_fusion_alg.py 
# Room 2: /home/team19/COSSY/utilities/execute_fusion_alg_room2.py

# Fusion results: /home/team19/COSSY/{time_stamped folder name}
# RP Sync results: /home/team19/COSSY/{RP1 or RP2 or RP3 or RP4}

# Plotting:

# /home/team19/COSSY/plotting/COSSY_plotting.py


## Notes:

# The output from the RAPID wrapper is redirected to file "running_stdout.txt" located in
# the wrapper's directory so that the stream of messages does not overwhelm the screen.

# The output from Rsync, that synchronizes door-sensor files with the NUC, is redirected to file
# "autoSync.txt" located in the current directory.

# JSON files from the door sensors are located in directories named "RP#"

# People-counting results are stored in directories with time-stamped names

