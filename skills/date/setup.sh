#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.date.service
touch /lib/systemd/system/rhasspy.skill.date.service
:> /lib/systemd/system/rhasspy.skill.date.service

echo "
[Unit]
Description=Rhasspy Volume Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/date.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.date.service

sudo rm -f date.sh
touch date.sh
:> date.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-date.py" >>  date.sh

chmod +x date.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.date.service
sudo systemctl stop rhasspy.skill.date.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.date.service
sudo systemctl start rhasspy.skill.date.service
sudo reboot
