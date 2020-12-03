#!/usr/bin/env bash

pip3 install python-vlc
pip3 install -r requirements.txt


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

sudo rm -f /lib/systemd/system/rhasspy.skill.musicplayer.service
touch /lib/systemd/system/rhasspy.skill.musicplayer.service
:> /lib/systemd/system/rhasspy.skill.musicplayer.service

echo "
[Unit]
Description=Rhasspy Musicplayer Skill
After=multi-user.target

[Service]
Type=simple
ExecStart=$SCRIPTPATH/musicplayer.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target

  " >>  /lib/systemd/system/rhasspy.skill.musicplayer.service

sudo rm -f musicplayer.sh
touch musicplayer.sh
:> musicplayer.sh

echo "#!/bin/bash
python3 $SCRIPTPATH/action-musicplayer.py" >>  musicplayer.sh

chmod +x musicplayer.sh


sudo sudo chmod 644 /lib/systemd/system/rhasspy.skill.musicplayer.service
sudo systemctl stop rhasspy.skill.musicplayer.service
sudo systemctl daemon-reload
sudo systemctl enable rhasspy.skill.musicplayer.service
sudo systemctl start rhasspy.skill.musicplayer.service
sudo reboot
