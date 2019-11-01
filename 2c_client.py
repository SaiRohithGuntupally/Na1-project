import sys
import socket

# parameters
host_ip = "localhost"
port_no = 12000

def connect(host_ip,port_no):
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host_ip,port_no))
	return s

def main():
	s=connect(host_ip, port_no)
	message=""
	while message !="exit":
	    message = input("Type Message:\n")
	    s.send(str.encode(message))
	s.close()
	print('connection closed')
	s.close()

if __name__== "__main__":
    main()
