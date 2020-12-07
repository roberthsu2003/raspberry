#!/bin/bash
# Script to start py app
# Add "/home/pi/startup_script.sh" to the end of /etc/rc.local

echo "Starting  take_picture_and_email ..."
sudo /home/pi/pygpio/take_picture_and_email.py &

