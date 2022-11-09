# This is server code to send video and audio frames over TCP

import socket
import threading, wave, pyaudio,pickle,struct
import binascii
import subprocess
from pydub import AudioSegment

host_name = socket.gethostname()
host_name = "localhost"
host_ip = '10.0.0.234'#  socket.gethostbyname(host_name)
# host_ip=socket.gethostbyname(host_name)
print(host_ip)
port = 9611

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((host_ip, port))

# UDPServerSocket.listen(5)
# UDPServerSocket.recvfrom(5)
print('server listening at',(host_ip, (port-1)))


def audio_stream(cli,f):
    CHUNK = 1024

    FRAMS_PER_BUFFER = 3200
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000

    wf = wave.open(f, 'rb')

    data = None
    while True:
        if cli:
            while True:
                data = wf.readframes(CHUNK)
                a = pickle.dumps(data)
                message = struct.pack("Q",len(a))+a
                # print("msg: ",message)
                client_socket.sendall(message)
                
# t1 = threading.Thread(target=audio_stream, args=())
# t1.start()

while True:
    # client_socket,addr = UDPServerSocket.accept()
    client_socket,addr = UDPServerSocket.recvfrom(1024)
    f="test1.wav"
    print("client: ",client_socket)
    print('address: ',addr)
    if client_socket:
        threading._start_new_thread( audio_stream, (client_socket,f))

