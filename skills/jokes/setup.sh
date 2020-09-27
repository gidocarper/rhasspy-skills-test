#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.jokes.service
touch /lib/systemd/system/rhasspy.skill.jokes.service
:> /lib/systemd/system/rhasspy.skill.jokes.service

echo "
[Unit]
Description=Rhasspy Jokes Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/jokes.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.jokes.service

sudo rm -f jokes.sh
touch jokes.sh
:> jokes.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-jokes.py" >>  jokes.sh

chmod +x jokes.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.jokes.service
sudo systemctl stop rhasspy.skill.jokes.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.jokes.service
sudo systemctl start rhasspy.skill.jokes.service
sudo reboot
