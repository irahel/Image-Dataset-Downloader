import urllib.request, os
import requests

NEW_PATH            = r'downloaded'
EXTENSION           = '.jpg'
ARCHIVE_NAME        = "base.txt"
PERMISSION_READ     = 'r'
PERMISSION_B_READ   = 'rb'
PERMISSION_WRITE    = 'w'
PERMISSION_B_WRITE  = 'wb'
TIMEOUT_MAX_WAIT    = 10

def downloader(image_url, count):
    #Create folder
    if not os.path.exists(NEW_PATH):
        os.makedirs(NEW_PATH)  

    full_file_name = f"{NEW_PATH}/{str(count)}{EXTENSION}"
    request = urllib.request.urlopen(image_url, timeout=TIMEOUT_MAX_WAIT)
    with open(full_file_name, PERMISSION_B_WRITE) as file:
        try:
            file.write(request.read())
        except:
            print("File creation error")    

print("Starting")
print("Trying open base archive")
with open(ARCHIVE_NAME, PERMISSION_READ) as base:
    for count, link in enumerate(base, start=1):
        print("Downloading image ",count)
        try:
            downloader(link.replace("\n", ""), count)         
            print("Sucessfull download image ", count)
        except:
            print("Error download image " ,count)
print("Ended")
        