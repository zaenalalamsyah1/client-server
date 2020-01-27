import socket #import socket library

# function which return reverse of a string
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return 'yes, it is Palindrome'
    return 'no, it is not'

def server_tcp():
    host = socket.gethostname() # get hostname or IP in used
    port = 43179  # Random port number

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # make a socket with IPv4 and TCP Protocol
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2) #Enable a server to accept connections , 2 meaning backlog

    print ("(+)Connection Server Ready to Get Message...") #message for tell user connection ready 

    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode() #recive data with buffersize 1024 from client
        if not data:
            # if data is not received break
            break
        print("Message from Client : " + str(data))
        conn.send(isPalindrome(data).encode())  # send data to the client result palindrome and set UPPERCASE

server_tcp() #run function of server_tcp()
