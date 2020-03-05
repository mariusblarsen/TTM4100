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

    # Set socket timeout as 1 second
    clientSocket.settimeout(timeout)


    # Sequence number of the ping message
    ptime = 0  
    RTT = 0.0

    # Ping for 10 times
    while ptime < 10: 
        ptime += 1
        try:
            # Record the "sent time"
            time_sent = time.time()
            print("time_sent:\t", time_sent)

            # Format the message to be sent as in the Lab description	
            data = "Ping\t" + str(ptime) + "\t" + str(time_sent) # message should be: Ping sequence_number time, where time is when the client sends the message

            # Send the UDP packet with the ping message
            clientSocket.sendto(data.encode(), (host, port))

            # Receive the server response
            serverResponse, _ = clientSocket.recvfrom(2048)
      
            # Record the "received time"
            time_received = time.time()
            print("time_received:\t", time_received)

            # Display the server response as an output
            print("server responded:\t", serverResponse.decode())
        
            # Round trip time is the difference between sent and received time
            RTT = time_received - time_sent
            print("RTT in s:\t", RTT)
            print("-"*50)

        except:
            # Server does not respond
            # Assume the packet is lost
            print("Request timed out.")
            continue

    # Close the client socket
    clientSocket.close()

if __name__ == "__main__":
    main()
