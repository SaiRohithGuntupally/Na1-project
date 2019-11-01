import socket
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("IP : ",host_ip)
except: print("Unable to get Hostname and IP")
#orgnal program strats here
from socket import *
serverName =  '10.205.4.139'
serverPort = 12002
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence1 = str(host_ip)
    sentence2 = " " + input('Enter a sentence')
    sentence = sentence1 + sentence2
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    string = modifiedSentence.decode()
    #word = sentence1  #word_list = string.split()  #print(' '.join([i for i in word_list if i not in word]))  #final= ' '.join([i for i in word_list if i not in word])  #print(final)
    if  string == 'Bye':
        break
clientSocket.close()
