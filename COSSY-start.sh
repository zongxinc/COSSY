#!/bin/bash

NUC="python3%/home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy.py"
NUC2="python3%/home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy_room2.py"
RP="python3_rpi-realtime-peoplecount/run.py"
Fusion="python3 utilities/execute_fusion_alg.py"
Fusion_2="python3 utilities/execute_fusion_alg_room2.py"

now=$(date +"%m-%d-%Y-%T")
room=""

while getopts "MCSOImsfR:h" opt;
do
    case "${opt}" in
            h) echo "- '-C' will set it to run analysis from images taken from the camera
- '-S' will set it to save images
- '-O' will set it to save images to a folder named after current time. 
- '-I' will read images in from a folder should you need to anaylze them as such
- '-M' used when there are two cameras in one room
- '-m' is to enable saving thermal frame data in the json files.
- '-s' is to enable single-person/baseline algorithm instead of the multiperson algorithm. For the multiperson algorithm, omit flag. 
- '-f' is going to save the output from the RP in a folder named after current time
- '-R [room number]' it will tell the system to look at which room's information. To decide which room the COSSY is going to run"
                exit 1
                ;;
            M) Fusion="${Fusion} -M"
                Fusion_2="${Fusion_2} -M"
                    ;;
            C) NUC="${NUC}%-c"
                NUC2="${NUC2}%-c"
                    ;;
            S) NUC="${NUC}%-s"
                NUC2="${NUC2}%-s"
                    ;;
            O) NUC="${NUC}%-o%/home/team19/Desktop/Axis_DL/Detection/YOLO/${now}/"
                NUC2="${NUC2}%-o%/home/team19/Desktop/Axis_DL/Detection/YOLO/${now}/"
                    ;;
            I) NUC="${NUC}%-i"
                NUC2="${NUC2}%-i"
                    ;;
            m) RP="${RP}_-m"
                    ;;
            s) RP="${RP}_-s"
                    ;;
            f) RP="${RP}_-f_${now}/"
                    ;;
            R) Fusion="${Fusion} -R ${OPTARG}"
                Fusion_2="${Fusion_2} -R ${OPTARG}"
                room="${OPTARG}"
                    
    esac
done

if [[ ${room} == "1" ]]
then
    cd result
    rm *.json
else
    cd result2
    rm *.json
fi
# echo "${NUC2}"
cd
cd Desktop
. /home/team19/Desktop/ENV/bin/activate
cd Axis_DL/Detection/YOLO
mkdir "${now}"
cd "${now}"
mkdir "Camera 1"
mkdir "Camera 2"
mkdir "Camera 3"
cd ..
cd 
cd COSSY
if [[ ${room} == "1" ]]
then
    echo "${NUC}"
    eval "python3 utilities/execute_camera_alg.py -p ${NUC} -R ${room}" &
else
    echo "${NUC2}"
    eval "python3 utilities/execute_camera_alg.py -p ${NUC2} -R ${room}" &
fi
# echo "${RP}"
eval "python3 utilities/execute_door_alg.py -p ${RP} -R ${room}"&
# ssh pi@10.241.10.17 "${RP}"&
# ssh pi@10.241.10.32 "${RP}"&
# echo "helo"
if [[ ${room} == "1" ]]
then
    python3 utilities/RP_sync.py >autoSync.txt&
else
    python3 utilities/RP_sync_room2.py >autoSync.txt&
fi
# echo "bello"
if [[ ${room} == "1" ]]
then
    echo "${Fusion}"
    eval "${Fusion}">filter.txt&
else
    echo "${Fusion_2}"
    eval "${Fusion_2}">filter.txt&
fi
