#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.calculator.service
touch /lib/systemd/system/rhasspy.skill.calculator.service
:> /lib/systemd/system/rhasspy.skill.calculator.service

echo "
[Unit]
Description=Rhasspy Calculator Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/calculator.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.calculator.service

sudo rm -f calculator.sh
touch calculator.sh
:> calculator.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-calculator.py" >>  calculator.sh

chmod +x calculator.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.calculator.service
sudo systemctl stop rhasspy.skill.calculator.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.calculator.service
sudo systemctl start rhasspy.skill.calculator.service
sudo reboot
