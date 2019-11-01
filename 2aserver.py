import socket
from socket import *
serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
def functon():
    try:    #useful when clent forcefully shutdowns
        while True:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024).decode()
            if sentence.startswith('192.168.222.1'):
                string = sentence
                word = '192.168.222.1'
                word_list = string.split()
                final= ' '.join([i for i in word_list if i not in word])
                connectionSocket.send(final.encode())
                connectionSocket.close()
                print(final)
                if sentence == '192.168.222.1 Bye':
                    break
    except:
        print("error in clientside")
        functon()
functon()
