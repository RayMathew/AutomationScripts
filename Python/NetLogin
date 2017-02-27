from selenium import webdriver
import wx
import subprocess
import ctypes

browser = webdriver.Chrome("X:\\...\\chromedriver.exe")#replace this with your location of webdriver
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
