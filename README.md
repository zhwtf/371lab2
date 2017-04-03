In this assignment, I developed a simple Web server in Python. 
The functions and features are listed below:
1. Create a connection socket when contacted by web browser, up to 5 connections can be allowed to wait in a queue ; 
2. Receive the HTTP request from this connection;
3. Parse the request to determine the specific file being requested; 
4. Get the requested file from the server’s file system; 
5. Create an HTTP response message consisting of the requested file preceded by header lines; 
6. Send the response over the TCP connection to the requesting browser. 

If a browser uses a non-compatible version of HTTP, the server will send “505 HTTP Version Not Supported” error message 
to a client. Also, if a browser requests a file that is not present in the server, the server will return
a “404 Not Found” error message.

