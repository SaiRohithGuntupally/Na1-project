import socket
import _thread
from _thread import start_new_thread

# parameters
host_ip=''
port_no=12002
client_list = []

def bind(host_ip,port_no):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host_ip,port_no))
	s.listen(5)
	return s


def client_broadcast(addr,strg):
	for i in client_list:
		a=str(addr)+str(strg)
		i.sendall(str.encode(a))

def client_thread(c,addr):
		print ("got connection from", addr)
		i=""
		while i != "exit":
			i=c.recv(1024).decode()
			print ("received", addr, i)
			start_new_thread(client_broadcast, (addr,i, ))
		print ("client connection closed", addr)
		c.close()
		client_list.pop(client_list.index(c))

def connect_clients(s):
	while True:
		c,addr=s.accept()
		client_list.append(c)
		start_new_thread(client_thread, (c,addr,))

def main():
	s=bind(host_ip, port_no)
	connect_clients(s)
	print ("connection closed with all the clients\n")
	s.close()

if __name__== "__main__":
	main()
