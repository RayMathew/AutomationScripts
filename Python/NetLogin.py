from selenium import webdriver
import wx
import subprocess
import ctypes

#The primary library for this script is webdriver, which needs to be downloaded and installed from here: 
#https://pypi.python.org/pypi/chromedriver_installer
#The other library is wxpython: https://www.wxpython.org/download.php. For a 32-bit computer, choose wxPython3.0-win32-py27 out of the 4 options.

MessageBox = ctypes.windll.user32.MessageBoxW

browser = webdriver.Chrome("X:\\...\\chromedriver.exe") #replace this with your location of webdriver
browser.get("http://portal.acttv.in/")

username = browser.find_element_by_name("_login_WAR_BeamPromotionalNDownloadsportlet_uname")
username.send_keys("*****")

password = browser.find_element_by_name("pword")
password.send_keys("*****")

password.submit()

browser.close()

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
x = ask(message = 'Start Hotspot?')

if x=="y":
    subprocess.call("netsh wlan start hostednetwork")
    ctypes.windll.user32.MessageBoxW(0,u"Hotspot Started!",u"", 1)
    MessageBox(None, u'Hotspot Started.', u'', 0)
