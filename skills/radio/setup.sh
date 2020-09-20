#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.radio.service
touch /lib/systemd/system/rhasspy.skill.radio.service
:> /lib/systemd/system/rhasspy.skill.radio.service

echo "
[Unit]
Description=Rhasspy Online Radio Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/radio.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.radio.service

sudo rm -f radio.sh
touch radio.sh
:> radio.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-radio.py" >>  radio.sh

chmod +x radio.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.radio.service
sudo systemctl stop rhasspy.skill.radio.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.radio.service
sudo systemctl start rhasspy.skill.radio.service
sudo reboot
