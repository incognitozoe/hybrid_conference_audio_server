# This is server code to send video and audio frames over TCP

import socket
import threading, wave, pyaudio,pickle,struct
import binascii
import subprocess
from pydub import AudioSegment
# import speech_recognition as sr


# #audio to bytes
# file = open("tagthis.mp4", "rb")
# allbytes = []
# while 1:
#   somebytes = file.read(1024)

#   if not somebytes:
#     break

#   chunk = ""
#   for byte in somebytes:
#     byte =  bin(ord(byte))
#     byte = byte[2:len(byte)]
#     padding = "0" * (8 - len(byte))
#     chunk += padding + byte

#   allbytes.append(chunk)



host_name = socket.gethostname()
# host_ip = '192.168.1.102'#  socket.gethostbyname(host_name)
host_ip=socket.gethostbyname(host_name)
print(host_ip)
port = 9611

def audio_stream():
    server_socket = socket.socket()
    server_socket.bind((host_ip, (port-1)))

    server_socket.listen(5)
    CHUNK = 1024

    FRAMS_PER_BUFFER = 3200
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000
    
    #mp3 example
    # files                                                                         
    # src = "test.mp3"
    # dst = "test.wav"

    # # convert wav to mp3                                                            
    # sound = AudioSegment.from_mp3(src)
    # sound.export(dst, format="wav")

    wf = wave.open("test1.wav", 'rb')
    
    p = pyaudio.PyAudio()
    # r = sr.Recognizer()
    # with sr.AudioFile('temp.wav') as source:
    #     audio = r.record(source)

    # wf = r.recognize_google(audio)
    print('server listening at',(host_ip, (port-1)))
   
    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 input=True,
    #                 frames_per_buffer=CHUNK)

    # stream = p.open(format=FORMAT,
    #                 channels=CHANNELS,
    #                 rate=RATE,
    #                 input=True,
    #                 frames_per_buffer=FRAMS_PER_BUFFER)
            
    client_socket,addr = server_socket.accept()
 
    data = None
    while True:
        if client_socket:
            while True:
                data = wf.readframes(CHUNK)
                a = pickle.dumps(data)
                message = struct.pack("Q",len(a))+a
                # print("msg: ",message)
                client_socket.sendall(message)
                
t1 = threading.Thread(target=audio_stream, args=())
t1.start()

# while True:
#     print('Waiting for the incoming connections')
#     cli, ip = server_socket.accept()
#     cli.send(bytes('CONNECT_SUCCESSFUL'))

#     'Start the new client thread'
#     threading._start_new_thread( NewClientSocketHandler, (cli, ip))

