import socket #import socket library


def client_tcp():
    host = socket.gethostname()  # get hostname or IP in used
    port = 43179  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # make a socket with IPv4 and TCP Protocol
    client_socket.connect((host, port))  # connect to the server

    print (">>> WELCOME TO CLIENT SERVER WITH TCP PROTOCOL <<<")
    print ("input some text to know palindrome or not")
    message = input(" -> ")  # take input
 
    while message.lower().strip() != 'exit': # if type exit will disconnected / type not exit will loop

            client_socket.send(message.encode())  # send text from message input to server
		
            data = client_socket.recv(1024).decode()  # receive response from server
		
            print('Message From Server: ' + data)  # show message in terminal
		
            message = input(" -> ")  # again take input
		
    client_socket.close()  # close the connection if input = "exit"


client_tcp() #run client function

