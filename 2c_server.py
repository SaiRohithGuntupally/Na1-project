import socket
import threading
from _thread import start_new_thread
serverPort = 12000
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
def bind(serverPort):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    return serverSocket

def client_thread(connectionSocket, addr):
    message=""
    while True:
        message=connectionSocket.recv(1024).decode()
        print("received",addr,message)
        print("Current Time =", current_time)
        if message == "exit":
            print("client connection closed",addr)
            print("Current Time =", current_time)
            connectionSocket.close()
            break
serverSocket=bind(serverPort)
while True:
    connectionSocket, addr = serverSocket.accept()
    start_new_thread(client_thread,(connectionSocket, addr))
serverSocket.close()
