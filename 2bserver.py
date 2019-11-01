import socket
from socket import *
serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
def functon():
    try:
        Controller = 1    #useful when clent forcefully shutdowns
        while True:
            connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(1024).decode()
            host_ip = message.split()[0]
            if Controller == 1 or host_detector == host_ip:
                host_detector = host_ip
                Controller = 0
                #word_list = message.split()
                #print(' '.join([i for i in word_list if i not in word]))
                final = ' '.join([i for i in message.split() if i not in host_ip])
                connectionSocket.send(final.encode())
                connectionSocket.close()
                print(final)
                if message == host_ip +' '+ 'Bye':
                    Controller = 1
    except:
        print("error in clientside")
        functon()
functon()
