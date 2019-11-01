#include <unistd.h>
#include <stdio.h>
#include <Winsock2.h>
#include <stdlib.h>
#include <Winsock2.h>
#include <string.h>
#define PORT 8080
#define BUFSIZE 1024
int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buf[BUFSIZE] = {0};

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address,sizeof(address))<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

   	if (listen(server_fd, 5) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Enter # of clients : ");
	int num;
	scanf("%d",&num);
	for(int j=1;j<=num;j++)
	{
		if ((new_socket = accept(server_fd, (struct sockaddr *)&address,(socklen_t*)&addrlen))<0)
	    {
	        perror("accept");
	        exit(EXIT_FAILURE);
	    }
	    memset(buf, 0, BUFSIZE);
		while (strcmp(buf,"exit")) {
			memset(buf, 0, BUFSIZE);
			int n = read( new_socket , buf, 1024);
		    printf("received : %s\n",buf);
		}
		printf("connection %d close \n", j);
	}
    return 0;
}
