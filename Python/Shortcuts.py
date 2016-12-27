import wx
import subprocess
import webbrowser
import os
import ctypes


#The primary library for this script is wxpython, which needs to be downloaded and installed from here: https://www.wxpython.org/download.php
#For a 32-bit computer, choose wxPython3.0-win32-py27 out of the 4 options.

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

app = wx.App()
app.MainLoop()

x = ask(message = 'Where to?')

MessageBox = ctypes.windll.user32.MessageBoxW

# This is where you can customize both the shortcut name and the shortcut target, according to your needs. Multiple names can be used to open the same target.
# The pseudo-code is: 
# if the user types "nameA" or "nameB" or ...:
# 	 then go to target "XYZ"
#
# The current capabilities of the script are: 
# 1. Open any folder using Windows Exlporer, using the subprocess.Popen() function.
# 2. Open any browser, and any website on it, using webbrowser.get().open() function.
# 3. Open a browser in incognito mode, by passing in the "-incognito" argument.
# 4. Open any file or application using it's default program using os.startfile() function.
# 5. Pass in commands to Commands Prompt using os.system() function. Administrator rights are not available.

# If you know how to pass commands to Command Prompt with Administrator privileges, or know of any useful capability that I've missed out,
# let me know here: https://github.com/RayMathew/AutomationScripts/issues by creating a New issue.
# Please also follow the pattern of slashes religiously, that indicate going into a folder. Some methods require double-backslashes("\\") or forward-slashes("/"), while others 
# understand the Windows single backslash ("\") format.

# opening a folder:
if x == "Downloads" or x == "d":
    subprocess.call("explorer C:\\Users\\RayM\\Downloads", shell=True)

#opening any website, using any browser:
elif x == "google":
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.co.in")

#opening a browser in incognito mode:
elif x == "GoogleI" or x == "googlei":
    subprocess.call("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito https://www.google.co.in", shell=True)

#opening a .exe app:
elif x == "steam" or x == "Steam":
    subprocess.call("C:\\Program Files (x86)\\Steam\\steam.exe")

#opening any application (including .exe) or file in it's default program:
elif x == "note":
	os.startfile("C:\\Users\\RayM\\Downloads\\hello.txt")
	
#sending commands to Command Prompt:
elif x =="EnvV" or x == "envv":
    os.system('rundll32.exe sysdm.cpl,EditEnvironmentVariables')

#using the windows error message dialogue box
elif x == "meow":
    MessageBox(None, u'meow!', u'', 0)
