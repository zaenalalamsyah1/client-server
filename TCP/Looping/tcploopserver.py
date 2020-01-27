import socket #import socket library


def server_tcp():
    # host name
    host = socket.gethostname() # get hostname or IP in used
    port = 43178  # Random port number

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # make a socket with IPv4 and TCP Protocol
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2) #Enable a server to accept connections , 2 meaning backlog

    print ("(+)Connection Server Ready to Get Message...") #message for tell user connection ready 
    
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Pesan dari Client: " + str(data))
        conn.send(data.upper().encode())  # send data to the client and set UPPERCASE

server_tcp() #run function of server_tcp()
