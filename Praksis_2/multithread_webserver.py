# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

# Import socket module
from socket import *
from _thread import *
import threading

print_lock = threading.Lock()


class clientThread(threading.Thread):
    def __init__(self, connectionSocket, addr):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.addr = addr

    def run(self):
        while True:
            try:
                # Receives the request message from the client
                message = self.connectionSocket.recv(1024)
                if not message:
                    print("No data, bye")
                    # print_lock.release() 
                    break

                print("Message: \n", message)
                # Extract the path of the requested object from the message
                # The path is the second part of HTTP header, identified by [1]
                filepath = message.split()[1]

                # Because the extracted path of the HTTP request includes
                # a character '\', we read the path from the second character
                f = open(filepath[1:])

                # Read the file "f" and store the entire content of the requested file in a temporary buffer
                outputdata = f.read()  # FILL IN START		# FILL IN END
                print("Outputdata: \n", outputdata)
                self.connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))

                # Send the content of the requested file to the connection socket
                response = outputdata + "\r\n"
                # connectionSocket.send(response) #Python 2.7
                self.connectionSocket.send(response.encode())  # Python 3

                # Close the client connection socket
                self.connectionSocket.close()

            except (IOError, IndexError):
                # Send HTTP response message for file not found
                # Same format as above, but with code for "Not Found" (see outputdata variable)
                self.connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))
                self.connectionSocket.send(bytes('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n', 'UTF-8'))

        # Close the client connection socket
        self.connectionSocket.close()

def main():
    # Create a TCP server socket
    # (AF_INET is used for IPv4 protocols)
    # (SOCK_STREAM is used for TCP)
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Assign a port number
    serverPort = 6789

    # Bind the socket to server address and server port
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)

    threads = []

    # Server should be up and running and listening to the incoming connections
    while True:
        print("socket is listening")

        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()

        # print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Starting new thread
        # start_new_thread(threaded, (connectionSocket,))
        new_thread = clientThread(connectionSocket, addr)
        new_thread.setDaemon(True)
        new_thread.start()
        threads.append(new_thread)


    serverSocket.close()


if __name__ == "__main__":
    main()
