#!/bin/bash

now=$(date +"%m-%d-%Y-%T")
NUC="python3%/home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy.py%-c"
NUC2="python3%/home/team19/Desktop/Axis_DL/Detection/YOLO/axis_cameras_single_cam_v2_copy_room2.py%-c"
RP="python3_rpi-realtime-peoplecount/run.py"
Fusion="python3 utilities/execute_fusion_alg.py"
Fusion_2="python3 utilities/execute_fusion_alg_room2.py"


room=""
single=""
cam=""
temperature="python3 collect_temp_info.py"

while getopts "OSsmR:hr:DAB" opt;
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
            # C) NUC="${NUC}%-c"
            #     NUC2="${NUC2}%-c"
            #         ;;
            # S) NUC="${NUC}%-s"
            #     NUC2="${NUC2}%-s"
            #         ;;
            O) NUC="${NUC}%-o%/home/team19/Desktop/Axis_DL/Detection/YOLO/${now}/"
                NUC2="${NUC2}%-o%/home/team19/Desktop/Axis_DL/Detection/YOLO/${now}/"
                RP="${RP}_-f_${now}/"
                Fusion="${Fusion} -f ${now}/"
                Fusion2="${Fusion2} -f ${now}/"
                temperature="${temperature} -d ${now}"
                    ;;
            D) Fusion="${Fusion} -D"
                    ;;
            S) NUC="${NUC}%-s"
                NUC2 = "${NUC2}%-s"
                    ;;
            s) RP="${RP}_-m"
                    ;;
            m) single="m"
                    ;;
            A) cam="${cam} -A"
                    ;;
            B) cam="${cam} -B"
                    ;;
            R) Fusion="${Fusion} -R ${OPTARG}"
                Fusion_2="${Fusion_2} -R ${OPTARG}"
                room="${OPTARG}"
                    ;;
            r) input="${OPTARG}"
                if [[ ${input} == "0" ]]
                then
                    temperature=""
                else
                    temperature="${temperature} -r ${OPTARG}"
                fi
                # echo "${input}"
                
                    
    esac
done

if [[ ${single} == "m" ]]
then
    RP="${RP}"
else
    RP="${RP}_-s"
fi

echo "${RP}"
echo "${Fusion}"
echo "${Fusion_2}"
echo "${NUC}"
echo "${NUC2}"
echo "${temperature}"


if [[ ${room} == "1" ]]
then
    mkdir "${now}"
else
    mkdir "room2_${now}"
fi
cd RP1
rm *.json
cd ..
cd RP2
rm *.json
cd ..
cd RP3
rm *.json
cd ..
cd RP4
rm *.json
cd ..
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
    eval "python3 utilities/execute_camera_alg.py -p ${NUC} -R ${room} ${cam}" &
else
    echo "${NUC2}"
    eval "python3 utilities/execute_camera_alg.py -p ${NUC2} -R ${room} ${cam}" &
fi
echo "helo"
echo "python3 utilities/execute_door_alg.py -p ${RP} -R ${room} ${temperature}"
eval "python3 utilities/execute_door_alg.py -p ${RP} -R ${room} ${temperature}"&
# ssh pi@10.241.10.17 "${RP}"&
# ssh pi@10.241.10.32 "${RP}"&

if [[ ${room} == "1" ]]
then
    python3 utilities/RP_sync.py >autoSync.txt&
else
    python3 utilities/RP_sync_room2.py >autoSync.txt&
fi
# echo "bello"
deactivate
if [[ ${room} == "1" ]]
then
    echo "${Fusion}"
    eval "${Fusion}"&
    #eval "${Fusion}"&
else
    echo "${Fusion_2}"
    eval "${Fusion_2}"&
fi
