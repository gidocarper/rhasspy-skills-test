#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.gasoline.service
touch /lib/systemd/system/rhasspy.skill.gasoline.service
:> /lib/systemd/system/rhasspy.skill.gasoline.service

echo "
[Unit]
Description=Rhasspy Gassoline Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/gasoline.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.gasoline.service

sudo rm -f gasoline.sh
touch gasoline.sh
:> gasoline.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-gasoline.py" >>  gasoline.sh

chmod +x gasoline.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.gasoline.service
sudo systemctl stop rhasspy.skill.gasoline.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.gasoline.service
sudo systemctl start rhasspy.skill.gasoline.service
sudo reboot
