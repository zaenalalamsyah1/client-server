import socket #import socket library

def mainmenu():
    print("Choose Menu :")
    print("1.Looping")
    print("2.Palindrome")
    selection = int(input(" -> "))

    if selection == 1:
        client_tcp()
    elif selection == 2:
        client_palin()



def client_tcp():
    host = socket.gethostname()  # get hostname or IP in used
    port = 43178  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # make a socket with IPv4 and TCP Protocol
    client_socket.connect((host, port))  # connect to the server

    print (">>> WELCOME TO CLIENT SERVER WITH TCP PROTOCOL <<<")
    print ("input some text to be UPPERCASE")
    message = input(" -> ")  # take input
 
    while message.lower().strip() != 'exit': # if type exit will disconnected / type not exit will loop

            client_socket.send(message.encode())  # send text from message input to server
		
            data = client_socket.recv(1024).decode()  # receive response from server
		
            print('Message From Server: ' + data)  # show message in terminal
		
            message = input(" -> ")  # again take input
		
    client_socket.close()  # close the connection if input = "exit"

def client_palin():
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

mainmenu()