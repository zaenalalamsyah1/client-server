import socket #import socket library

def reverse(string): #make function reverse string
    return string[::-1]

def palindrome(string): 
    rev = reverse(string) #call function reverse string

    if (string == rev):
        return 'yes, it is palindrome'
    return 'no, its not'

def server_udp():
    host = socket.gethostname() # get hostname or IP in used
    port = 1995 #port random number

    #create socket 
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # make a socket with IPv4 and UDP Protocol
    serversocket.bind((host,port)) #bin host and port together

    print ("(+)Connection Server Ready to use...")
    
    while True:
		
        message, client_addr = serversocket.recvfrom(2048)
		
        print("message from client :", message.decode())
		
        print("From :", client_addr)

        print("Send Response to Client..")
		
        modifiedMessage = message.decode()

        serversocket.sendto(palindrome(modifiedMessage).encode(),client_addr) #send palindrom message


server_udp() #run function