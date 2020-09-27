#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.volume.service
touch /lib/systemd/system/rhasspy.skill.volume.service
:> /lib/systemd/system/rhasspy.skill.volume.service

echo "
[Unit]
Description=Rhasspy Volume Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/volume.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.volume.service

sudo rm -f volume.sh
touch volume.sh
:> volume.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-volume.py" >>  volume.sh

chmod +x volume.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.volume.service
sudo systemctl stop rhasspy.skill.volume.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.volume.service
sudo systemctl start rhasspy.skill.volume.service
sudo reboot
