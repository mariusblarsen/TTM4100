import time
import sys
from socket import * # Don't need to specify socket.method()

# Get the server hostname and port as command line arguments                    
host =  sys.argv[0]
port = sys.argv[1]
timeout = 1 # in seconds
 
# Create UDP client socket
clientSocket = socket(AT_INET, SOCK_DGRAM)
clientSocket.bind((host, port))

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)


# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data = # FILL IN START		# FILL IN END
    
    try:
    	# FILL IN START
    	
	# Record the "sent time"

	# Send the UDP packet with the ping message

	# Receive the server response
  
	# Record the "received time"

	# Display the server response as an output
    
	# Round trip time is the difference between sent and received time

        
        # FILL IN END
    except:
        # Server does not respond
	# Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientsocket.close()
 
