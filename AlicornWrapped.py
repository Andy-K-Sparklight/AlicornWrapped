import os
import sys
import requests
import zipfile
import getpass

# Alicorn Wrapper for Windows
# This URL is hard coded and should always stay there, while we can change on GitHub
al_Origin = "https://endpoint.fastgit.org/https://github.com/Andy-K-Sparklight/AlicornBinaries/releases/download/latest/Alicorn-win32-x64.zip"
home = "C:\\Users\\" + getpass.getuser() # Build home dir

al_Root = home + "\Alicorn-win32-x64" # Specified name
al_Compressed = home + "\AlicornBinary.zip" # Download Temp
al_Executable =  al_Root + "\Alicorn.exe" # Alicorn Executable

# UnZip
def un_zip(f):
    z = zipfile.ZipFile(f)
    if os.path.isdir(al_Root):
        pass
    else:
        os.mkdir(al_Root)
    for names in z.namelist():
        z.extract(names, home + "\\")
    z.close()

# Run if exists
if os.access(al_Executable, os.X_OK):
    print("Alicorn Found! Starting...")
    os.system("cd " + al_Root + " && start /B Alicorn.exe")
    sys.exit(0)

# Download and unpack
else:
    print("Please wait... This may take up to 1 minute.")
    f = requests.get(al_Origin)
    with open(al_Compressed, "wb") as d:
        d.write(f.content)
    print("Unpacking objects...")
    un_zip(al_Compressed)

# Can run?
if os.access(al_Executable, os.X_OK):
    print("Alicorn Found! Starting...")
    os.system("cd " + al_Root + " && start /B Alicorn.exe")
    sys.exit(0)
else:
    # If no execute permission or not exist
    print("Failed to launch Alicorn! Press Enter to continue...")
    input()
    sys.exit(1)
