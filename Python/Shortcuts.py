import wx
import subprocess
import webbrowser
import os
from subprocess import call

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

# Initialize wx App
app = wx.App()
app.MainLoop()

# Call Dialog
x = ask(message = 'Where to?')

if x == "CA" or x == "ca" or x == "ComputerAwesomeness" or x == "CompAwesomeness":
    subprocess.Popen(r'explorer /select,"X:\Studies Stuff\Computer Awesomeness\"')

elif x == "RecentDownloads" or x == "RD" or x == "rd":
    subprocess.Popen(r'explorer /select,"X:\Recent Downloads"')

elif x == "Downloads" or x == "downloads":
    subprocess.Popen(r'explorer /select,"C:\Users\RayM\Downloads"')

elif x == "FProfile" or x == "fprofile":
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.facebook.com/ray.mathew.967")

elif x == "AddLifeEvent" or x == "flifeevent":
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").\
        open("https://www.facebook.com/ray.mathew.967/about?section=year-overviews&pnref=about")

elif x == "QuoraMs"or x == "qms" or x == "QuoraMessages" or x == "QuoraM":
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.quora.com/messages/")

elif x == "QuoraQs"or x == "qqs" or x == "quoraqs":
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.quora.com/answer")

elif x == "GoogleI" or x == "googlei":
    call("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito https://www.google.co.in", shell=True)

elif x == "steam" or x == "Steam":
    subprocess.call("C:\\Program Files (x86)\\Steam\\steam.exe")

elif x =="EnvV" or x == "envv":
    os.system('rundll32.exe sysdm.cpl,EditEnvironmentVariables')
