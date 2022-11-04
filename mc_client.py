import socket

clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clisocket.connect(('localhost', 9913))
print('The client has been connected')

print('The message from server.', clisocket.recv(256).decode())

print('Please keep providing the messages to send to server...')

while True:
    msg = input('Please write the message (string in quotes):')
    clisocket.send(bytes(msg))