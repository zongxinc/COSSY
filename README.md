# BOSTON UNIVERSITY
# COSSY - Computational Occupancy Sensing System  

# Setting up COSSY in a new deployment.
## You must have IP addresses for all devices (MAC addresses)

cd cossy
python3 COSSY-setup.py

## Answer all questions. Sensor and camera IDs are printed on each device.
## Make sure all the answers are correct so that the system can connect to all devices. 


# Starting COSSY
## Make sure that no one stands under door sensors for the first 10 sec of system operation.

cd cossy
bash COSSY-start.sh [flags]

## Flags:
## `-R [room number]` run COSSY in room number 1 or 2
## `-O` save the result from Camera, RP and Fusion in directory with name corresponding to current time 
## `-s` (optional)save the RP thermal frame into the result folder as well
## `-m` (optional)using multi-people algorithm on the RP, if not specified, RP will use the single-people algorithm

## Example: run COSSY in room #1:

bash COSSY-start.sh -O -R 1 &

## Example: run COSSY in room #2 and save the thermal frame:

bash COSSY-start.sh -O -R 2 -s &


# Stopping COSSY: first hit "Enter" on the keyboard (to get the prompt) and then

bash COSSY-stop.sh [flags]

## Flags:
## `-R [room number]` stop COSSY running in room 1 or 2

## Example: to stop COSSY running in room 1:

bash COSSY-stop.sh -R 1

## Ploting

When tried to graph, go to the `plotting` folder uses:
`python3 dataMatch.py -f [result folder name]`
eg:
`python3 dataMatch.py -f 05-11-2021-03:04:47/`
Remember to add `/` at the end


# Notes:

## The output from the RAPID wrapper is redirected to file ```running_stdout.txt``` located in
## the wrapper's directory so that the stream of messages does not overwhelm the screen.

## The output from Rsync, that synchronizes door-sensor files with the NUC, is redirected to file
## ```autoSync.txt``` located in the current directory.

## JSON files from the door sensors are located in directories named ``RP#''

## People-counting results are stored in directories with the name of execution time

##
