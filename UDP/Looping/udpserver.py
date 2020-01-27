import socket #import socket library

def server_udp():
	host = socket.gethostname() # get hostname or IP in used
	port = 2020 #port random number

	#create UDP Socket 
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # make a socket with IPv4 and UDP Protocol
	serversocket.bind((host,port)) # bind host address and port together

	print ("(+)Connection Server Ready to use...")
	while True:
		message, client_addr = serversocket.recvfrom(2048) # recive from client
		print("message from client :", message.decode()) 
		print("From :", client_addr)

		print("Send Response to Client..")
		modifiedMessage = message.decode().upper() #send message with uppercase
		serversocket.sendto(modifiedMessage.encode(),client_addr)

server_udp() #run function