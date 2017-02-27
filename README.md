# AutomationScripts

This is a fun personal project to learn automation. As of now (25th Sept 2016) I'm focusing on Python in Windows OS alone, and kiddie scripts at that.
Download and use freely. Open them with a Text Editor first, to see further instructions on how to use them.


Summary Of Scripts:
  1. ChromeOpenSites.py:
  
      Opens your Chrome browser with a specific list of websites. You can change the list as well as the browser.
      
  2. ResizeImage.py:
  
      Reduces the size of all images in a folder to the dimensions specified inside the script. Original images remain unaltered.
   
  3. Shortcuts.py:
  
      Enables you to open any application, file or folder that doesn't require Administrator privileges. Set the target yourself, as    well as the input name for it. Examples are given in the script. 
      Tip: Save this script anywhere in your computer, create a shortcut, and save the shortcut in C:\ProgramData\Microsoft\Windows\Start Menu\Programs. Then give it a shortcut key by right clicking on it and selecting Properties --> Shortcut --> Shortcut key. This allows you to call the script from anywhere, which is the whole point of it anyway.
      
  4. NetConnectionCheck.py:
  
      Checks whether an internet connection is available for your computer, by contacting a DNS server with a website of your choice. It's useful when your ISP has an unplanned downtime and you don't want to waste time reloading a webpage every few minutes to check if it's back up. It plays an alarm to alert you when the net connection is re-established. Tip: You could add this script to the list of shortcuts in Shortcuts.py above. 
      
  5. NetConnectionCheckJazzed.py:
    
      It performs the same function as NetConnectionCheck.py, and also plays a slideshow of pictures from a folder of your choice while the net connection check is done in the background. When the net connection is re-established the slideshow closes on its own. If you understand how to code in Python, this slideshow can be replaced with any other distraction, like a video, a song, a movie, etc. Tip: You could add this script to the list of shortcuts in Shortcuts.py above. 
      
  6. NetLogin.py:
 
    It logs into my internet portal and then asks if the Wi-Fi hotspot should be started. If you type 'y' a confirmation dialog box pops up. Windows Task Scheduler runs this script when the computer starts up.



All Python scripts have been written with version 2.7 - you need to install it in your computer for these scripts to work (https://www.python.org/downloads/release/python-2711/). For 32-bit Windows, choose Windows x86 MSI installer from the link.


You could run these scripts with Windows' Task Scheduler. For example, every time a user logs on, Chrome opens with your pre-defined list of websites.

