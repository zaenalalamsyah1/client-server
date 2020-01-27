import socket #import socket library

def client_udp():
    host = socket.gethostname() # get hostname or IP in used
    port = 1995 #port number server
    server = (host,port)

    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # make a socket with IPv4 and UDP Protocol

    print (">>> WELCOME TO CLIENT SERVER WITH UDP PROTOCOL <<<")
    print ("input some text to predict Palindrome or not")
    message = input("type text : ")

    while message.lower().strip() != 'exit': # if type exit will disconnected / type not exit will loop
        clientsocket.sendto(message.encode(), server) # send text from message input to server

        msgfromserver, server_addr = clientsocket.recvfrom(2048) # receive response from server
        
        print("Message from server :", msgfromserver.decode()) #print message from server
        
        message = input("type text: ") #input again

    clientsocket.close() #close socket if type exit

client_udp() #run function