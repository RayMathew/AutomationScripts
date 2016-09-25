import webbrowser

#Add website URLs in double quotes at the end of the list below. Don't forget to add a comma (,) between URLs.
sites = [
    "https://www.facebook.com/",
    "https://www.google.com/gmail/",
    "https://twitter.com/"
]
#To use any other browser, give the complete path like below. Do not remove the '%s', and either use single forward slashes (/) or
# double backward slashes (\\) to denote going into a file (In Windows).
for s in sites:
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(s)
