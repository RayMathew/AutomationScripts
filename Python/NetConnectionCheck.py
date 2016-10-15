import socket
import os
import time
import subprocess

# This is a simple check to see if net connection is available. I use it to alert me when the connection returns after
# my ISP has an unplanned downtime. I borrowed most of the code from StackOverFlow.

# I have given the name of my ISP's website here (since I need to log in from their home page to use my net), but this script will
# work with any website.
REMOTE_SERVER = "portal.acttv.in"
def is_connected():
  try:
    print "Checking"
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    # I decided to play Windows' Alarm sound to alert me when the net connection is available, but you can open
    # any audio, video, image or text file using the following function.
    os.startfile("C:\Windows\Media\Alarm01.wav")
    print "Connected"
  except:
     # Here you enter how many seconds the script should wait before it checks for the connection again.
     time.sleep(60)
     print "Net Connection Unavailable"
     is_connected()


is_connected()


