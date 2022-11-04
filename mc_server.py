import socket
import threading

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

srvsocket.bind(('localhost', 9913))
print('Bind to the local port')

srvsocket.listen(5)
print('Started listening...')

'New Client Thread'
def NewClientSocketHandler(cli, ip):
    print('The new client has socket id:', cli)
    while True:
        print('The message got for client socket:', cli)
        print(cli.recv(256).decode())

while True:
    print('Waiting for the incoming connections')
    cli, ip = srvsocket.accept()
    cli.send(bytes('CONNECT_SUCCESSFUL'))

    'Start the new client thread'
    threading._start_new_thread( NewClientSocketHandler, (cli, ip))