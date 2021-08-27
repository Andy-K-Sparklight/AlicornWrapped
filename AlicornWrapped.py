import os
import sys
import requests
import zipfile
import getpass
import time

al_Origin = "https://alicorn-go.vercel.app/latest-win32-release"
home = "C:\\Users\\" + getpass.getuser()

al_Root = home + "\\Alicorn-win32-x64"
al_Compressed = home + "\\AlicornBinary.zip"
al_Executable =  al_Root + "\\Alicorn.exe"

def downloadFile(name, url):
    headers = {'Proxy-Connection':'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size = 512):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'MiB/s')
                time1 = time.time()
    f.close()
    
def formatFloat(num):
    return '{:.2f}'.format(num)

def un_zip(f):
    z = zipfile.ZipFile(f)
    if os.path.isdir(al_Root):
        pass
    else:
        os.mkdir(al_Root)
    for names in z.namelist():
        z.extract(names, home + "\\")
    z.close()

if os.access(al_Executable, os.X_OK):
    print("Alicorn Found! Starting...")
    os.system("cd /d " + al_Root + " && start /B Alicorn.exe")
    sys.exit(0)

else:
    print("Please wait... This may take up to 1 minute.")
    print("If it's too slow you can press <Ctrl-C> to stop and try again.")
    downloadFile(al_Compressed, al_Origin)
    print("Unpacking objects...")
    un_zip(al_Compressed)
if os.access(al_Executable, os.X_OK):
    print("Alicorn Found! Starting...")
    os.system("cd " + al_Root + " && start /B Alicorn.exe")
    sys.exit(0)
else:
    print("Failed to launch Alicorn! Press Enter to continue...")
    input()
    sys.exit(1)
