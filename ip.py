import socket
import os
import time

print(f'Current IP: {socket.gethostbyname(socket.gethostname())}')

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

e = input("")
if e == 'info' or e == 'c':
    if e == 'info':
        while True:
                os.system('cls')
                print(f"Displays Local IP ({socket.gethostbyname(socket.gethostname())}) On Windows Systems")
                time.sleep(0.2)
                os.system('cls')
                print(f"Displays Local IP ({socket.gethostbyname(socket.gethostname())}) On Windows Systems.")
                time.sleep(0.2)
                os.system('cls')
                print(f"Displays Local IP ({socket.gethostbyname(socket.gethostname())}) On Windows Systems..")
                time.sleep(0.2)
                os.system('cls')
                print(f"Displays Local IP ({socket.gethostbyname(socket.gethostname())}) On Windows Systems...")
                time.sleep(0.2)
                continue
                
    elif e == 'c': 
       addToClipBoard(socket.gethostbyname(socket.gethostname()))
       os.system('cls')
       print(f"Coppied {socket.gethostbyname(socket.gethostname())} to clipboard")
       time.sleep(0.2)
       os.system('cls')
       print(f"Coppied {socket.gethostbyname(socket.gethostname())} to clipboard.")
       time.sleep(0.2)
       os.system('cls')
       print(f"Coppied {socket.gethostbyname(socket.gethostname())} to clipboard..")
       time.sleep(0.2)
       os.system('cls')
       print(f"Coppied {socket.gethostbyname(socket.gethostname())} to clipboard...")
       time.sleep(0.2)
        
    