import wx
import subprocess
import webbrowser
import os
import ctypes


#The primary library for this script is wxpython, which needs to be downloaded and installed from here: https://www.wxpython.org/download.php
#For a 32-bit computer, choose wxPython3.0-win32-py27 out of the 4 options.

MessageBox = ctypes.windll.user32.MessageBoxW

x = ""

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
	#The location of the txt file, from where key-value pairs are dynamically taken and displayed in the application. These key-value
	#pairs show the code or phrase you have to enter to perform a particular function.
        text_file = open("Shortcuts\\keyvalueForShortCuts.txt", "r")
        lines = text_file.read().split('\n')
        text_file.close()

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='Shortcuts', pos=(130, 45))
        heading.SetFont(font)

        wx.StaticLine(self, pos=(25, 80), size=(300, 1))
        posy = 110
        for line in lines:
            line = line.split("=")[0]
            wx.StaticText(self, label=line, pos=(25, posy))
            posy+=20

        posy = 110
        for line in lines:
            line = line.split("=")[1]
            wx.StaticText(self, label=line, pos=(250, posy))
            posy+=20

        wx.StaticLine(self, pos=(25, posy+20), size=(300, 1))
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT, pos=(25, posy+40), size=(300,22))
        btn = wx.Button(self, label='Close', pos=(80, posy+80))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        btn1 = wx.Button(self, label='OK', pos=(180, posy + 80))
        btn1.Bind(wx.EVT_BUTTON, self.OnOk)
        self.display.Bind(wx.EVT_TEXT_ENTER, self.OnOk)


        toolbar = self.CreateToolBar()
        qtool = toolbar.AddLabelTool(wx.ID_ANY, 'OpenKeyValue', wx.Bitmap('Shortcuts\\circle.png'))
        toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.OpenKeyValue, qtool)


        self.SetSize((360, posy+180))
        self.SetBackgroundColour(wx.WHITE)
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        self.Close(True)

    def OpenKeyValue(self, e):
	#This function enables us to open the key-value txt file if we require, and make changes to it.
        os.startfile("Shortcuts\\keyvalueForShortCuts.txt")

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

     def OnOk(self, e):
        x = self.display.GetValue()
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

	#Add/Remove Programs shortcut:
	elif x == "arp":
    		os.system('rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl')

	#starting and stopping wifi hotspot:
	elif x =="starths":
    		subprocess.call("netsh wlan start hostednetwork")

	elif x=="stophs":
    		subprocess.call("netsh wlan stop hostednetwork")

	#using the windows error message dialogue box
	elif x == "meow":
    		MessageBox(None, u'meow!', u'', 0)
	self.Destroy()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
