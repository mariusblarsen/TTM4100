import time
import sys
from socket import * # Don't need to specify socket.method()

# Get the server hostname and port as command line arguments                    
def main():
    host =  sys.argv[1]
    print("host: ", host)
    port = int(sys.argv[2])
    print("port: ", port)
    timeout = 1 # in seconds
     
    # Create UDP client socket
    clientSocket = socket(AF_INET, SOCK_DGRAM) #Internet and UDP
    clientSocket.bind((host, port))

    # Set socket timeout as 1 second
    clientSocket.settimeout(timeout)


    # Sequence number of the ping message
    ptime = 0  

    # Ping for 10 times
    while ptime < 10: 
        ptime += 1
        # Format the message to be sent as in the Lab description	
        data = "Ping " + ptime # message should be: Ping sequence_number time, where time is when the client sends the message
        
        try:
            # Record the "sent time"
            time_sent = time.time()

            # Send the UDP packet with the ping message
            clientSocket.sendto(data.encode(), (host, port))

            # Receive the server response
            serverResponse, _ = clientSocket.recvfrom(2048)
      
            # Record the "received time"
            time_received = time.time()

            # Display the server response as an output
            print("server responded: ", serverResponse.decode())
        
            # Round trip time is the difference between sent and received time
            RTT = time_received - time_sent

            
        except:
            # Server does not respond
            # Assume the packet is lost
            print("Request timed out.")
            continue

    # Close the client socket
    clientsocket.close()

if __name__ == "__main__":
    main()
