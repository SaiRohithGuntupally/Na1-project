import sys
import socket
import _thread
from _thread import start_new_thread

serverName = '192.168.1.152'
serverPort = 12002

def connect(serverName,serverPort):
	clientSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	return clientSocket

def client(clientSocket):
    while 1:
        text=clientSocket.recv(1024)
        if not text: break
        print(text.decode())

def connect_client(clientSocket):
	message=""
	start_new_thread(client, (clientSocket,))
	while message !="exit":
		message=input("enter message:\n")
		clientSocket.send(str.encode(message))
	clientSocket.close()
	print ("connection closed")


clientSocket=connect(serverName, serverPort)
connect_client(clientSocket)
clientSocket.close()
