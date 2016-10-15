import socket
import os
import time
import subprocess
import win32com.client
import win32gui
import win32process

# This is an unnecessary, fun and jazzed up version of my other script NetConnectionCheck.py. It continuously checks if net connection
# is available in the background, while it automatically starts up a slideshow for you. It requires installation of the pypiwin32 library
# at https://pypi.python.org/pypi/pypiwin32. Out of the downloads, choose among the two MS Windows Installers, depending on your system being
# 32 or 64 bit.

REMOTE_SERVER = "portal.acttv.in"
def is_connected():
  try:
    print "Checking"
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    os.startfile("C:\Windows\Media\Alarm01.wav")

    #The following lines of code can be changed as per your needs. Read on for further explanations.
    shell.AppActivate(pidphotos)
    time.sleep(2)
    shell.SendKeys("e", 0)
    time.sleep(2)
    shell.SendKeys("%{F4}", 0)
    # Up to here ###############

    print "Connected"

  except:
     time.sleep(60)
     print "You look fat. Go get some exercise."
     is_connected()

##########################################################################################################
# Beginning of unnecessary stuff

# The win32 library allows me to switch any application to the foreground or background. It also has a function to get an application's
# process ID, which allows me to send keyboard presses to it, and kill it if necessary.
# Over here I'm opening a folder with pictures, then opening a particular picture, and starting a slideshow by simulating the press of
# 'F5' button. It's important to use the time.sleep(s) function to make the script wait at appropriate points, otherwise the key presses
#  are sent before the previous task completes.

shell = win32com.client.Dispatch('WScript.Shell')
subprocess.Popen(r'explorer /select,"C:\Windows\Web\Wallpaper\Theme1\Deadpool-Red-Wallpaper-Background.jpg"')
time.sleep(2)

explorer = win32gui.GetForegroundWindow()
shell.SendKeys("{Enter}", 0)
time.sleep(2)

photos = win32gui.GetForegroundWindow()
# I'm getting the process ID of the application used to view the pictures, so that the script can automatically close it for me once
# the net connection is available.
_,pidphotos = win32process.GetWindowThreadProcessId(photos)
print(pidphotos)
shell.SendKeys("{F5}", 0)
time.sleep(2)

#End of unnecessary stuff
###########################################################################################################

is_connected()


