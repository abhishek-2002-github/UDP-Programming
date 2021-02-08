import socket
import os
import threading
import time

os.system("clear")

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "192.168.225.78"
port = 5555
os.system("tput setaf 2")
print("\t\t\t Abhi's Chat App... ")
os.system("tput setaf 6")
print("\t\t\t ------------------ ")
server.bind((ip,port))

def sender():
    data = ""
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    os.system("tput setaf 3")
    print("Enter the server IP: ")
    os.system("tput setaf 7")
    server_ip = input()
    server_port = 1234
    os.system("tput setaf 3")
    print("Enter your name :-")
    os.system("tput setaf 7")
    name = input()
    os.system("tput setaf 4")
    print("\n   Connecting Port 1234.... " )
    os.system("tput setaf 2")
    os.system("sleep 1")
    print("   Connected\n")
    os.system("tput setaf 7 ")
    print("  Joined into Chat Server as - %s" %name)
    print()
    os.system("tput setaf 1 ")
    print("\t\t----------CHAT WINDOW---------- \n")
    os.system("tput setaf 5")
    while True:
        if "Bye" in data or "bye" in data or "Exit" in data or "Tata" in data or "exit" in data:
            os.system("tput setaf 2")
            print("\n\tChat Window Closed !!! \n")
            os.system("tput setaf 7")
            os._exit(1)
        
        data = input()    
        final_data = "\t\t\t\t>  " + name + " : " + data
        client.sendto(final_data.encode() , (server_ip, server_port))

def receiver():
    while True:
        x = server.recvfrom(1024)
        clientIP = x[1][0]
        os.system("tput setaf 6")
        print(x[0].decode())      
        os.system("tput setaf 5")


send = threading.Thread( target = sender )
recv = threading.Thread( target = receiver )

send.start()
recv.start()  

