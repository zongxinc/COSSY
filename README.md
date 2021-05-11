# BOSTON UNIVERSITY
# COSSY - Computational Occupancy Sensing SYstem  

## Setting up COSSY in a new deployment.
# You must have IP addresses for all devices (MAC addresses)

cd cossy
python3 COSSY-setup.py

# Answer all questions. Sensor and camera IDs are printed on each device.
# Make sure all the answers are correct so that the system can connect to all devices. 


## Starting COSSY
# Make sure that no one stands under door sensors for the first 10 sec of system operation.

cd cossy
bash COSSY-start.sh [flags]

# Flags:
# `-R [room number]` run COSSY in room number 1 or 2
# `-O` save the result from Camera, RP and Fusion in directory with name corresponding to current time 
# `-s` (optional)save the RP thermal frame into the result folder as well
# `-m` (optional)using multi-people algorithm on the RP, if not specified, RP will use the single-people algorithm

# Example: run COSSY in room #1:

bash COSSY-start.sh -O -R 1 &

# Example: run COSSY in room #2 and save the thermal frame:

bash COSSY-start.sh -O -R 2 -s &


## Stopping COSSY: first hit "Enter" on the keyboard (to get the prompt) and then

bash COSSY-stop.sh [flags]

# Flags:
# `-R [room number]` stop COSSY running in room 1 or 2

# Example: to stop COSSY running in room 1:

bash COSSY-stop.sh -R 1

# Ploting

When tried to graph, go to the `plotting` folder uses:
`python3 dataMatch.py -f [result folder name]`
eg:
`python3 dataMatch.py -f 05-11-2021-03:04:47/`
Remember to add `/` at the end


## Notes:

# The output from the RAPID wrapper is redirected to file ```running_stdout.txt``` located in
# the wrapper's directory so that the stream of messages does not overwhelm the screen.

# The output from Rsync, that synchronizes door-sensor files with the NUC, is redirected to file
# ```autoSync.txt``` located in the current directory.

# JSON files from the door sensors are located in directories named ``RP#''

# People-counting results are stored in directories `result' and/or `result2`

## 
# Fusion

## To setup the roominformation

```
python3 COSSY-setup.py
```
And answer the problem one by one. Please make sure all the answers are correct so that the system can connect to the right devices. 

## To start

use ```bash COSSY-start.sh [flgs]```to start.

Capital letters are flags for the cameras or Fusion (-N is the only flag for the fusion):
  - `-C` will set it to run analysis from images taken from the camera
  - `-S` will set it to save images
  - `-O` will set it to save images to a folder named after current time. 
  - `-I` will read images in from a folder should you need to anaylze them as such
  - `-M` used when there are two cameras in one room
  - `-m` is to enable saving thermal frame data in the json files.
  - `-s` is to enable single-person/baseline algorithm instead of the multiperson algorithm. For the multiperson algorithm, omit flag. 
  - `f` is going to save the output from the RP in a folder named after current time
  - `-R [room number]` it will tell the system to look at which room's information. To decide which room the COSSY is going to run

eg: to run room 1 which has 2 cameras
```bash
bash COSSY-start.sh -C -S -O -M -I -m -s -f -R 1&
```
eg: to run room 2 which has 1 cameras
```bash
bash COSSY-start.sh -C -S -O -I -m -s -f -R 2&
```

## To End

To stop the program press enter and use:
eg: end the system in room 1
```bash
bash COSSY-stop.sh -R 1
```
- `-R [room number]` it will tell the system to end the system at which room

## Note
- I redirected the output from the camera to a file ```running_stdout.txt``` located at the same place where the camera's people counting program is on so that the constant output from the camera does not obstruct further operation.
- I also redirected the output from the Rsync to ```autoSync.txt``` located in the current directory.
- JSON files from the thermal sensor is located in folders call RP#
- Results are store in ```result``` or ```result2```


## 

