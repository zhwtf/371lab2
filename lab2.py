#import socket module
from socket import *
def main():
    serverPort = 1995
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    serverSocket.bind(('',serverPort))
    # 5 connections can be allowed to wait in a queue
    serverSocket.listen(1)
    #Fill in start
    #Fill in end
    while True:
    #Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            print message, '::',message.split()[0],':',message.split()[1]
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            print outputdata
            #Send one HTTP header line into socket

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
                connectionSocket.close()
        except IOError:
            pass
            print "404 Not Found"
            connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')
        break
    pass

if __name__ == '__main__';
    main()
