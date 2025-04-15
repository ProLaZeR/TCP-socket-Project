import socket
import threading
from tqdm import tqdm  # Make sure to install tqdm with: pip install tqdm
import struct
import os

serverInfo = ('127.0.0.1', 9999)
BUFFER_SIZE = 4096  # Use this variable for the buffer size

# Create and connect the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(serverInfo)
print('Connection to SERVER', serverInfo, 'established')

# Specify the file you want to send
filepath = "path/to/your/file.jpg"  # Update this with your actual file path
filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

# Send the header: filename length, filename, and filesize
client_socket.sendall(struct.pack('!I', len(filename)))
client_socket.sendall(filename.encode())
client_socket.sendall(struct.pack('!Q', filesize))
print(f"Sending file: {filename} with size: {filesize} bytes")

# Open the file in binary mode and send its contents with a progress bar
with open(filepath, "rb") as f:
    progress = tqdm(total=filesize, unit='B', unit_scale=True, desc=filename)
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)
        progress.update(len(bytes_read))
    progress.close()

print("File sent successfully.")
client_socket.close()

"""
try:
    while True:
        msg = input( "Message To Server : " )
        if not msg:
            break
        print( 'Client Sending -> ' + msg )
        sock.send( msg.encode( ) )
        serverReply = sock.recv( clientBufferSize ).decode( )
        print( 'Server Replied -> ' + serverReply )
except Exception as e:
    print( e )
finally:
    print('closing socket')
    sock.close()
    

def SendToServer( ):
    global sock
    msg = input( "Message To Server : " )
    if msg:
        print( 'Client Sending -> ' + msg )
        sock.send( msg.encode( ) )
    return msg

def GetServerReply( ):
    global sock
    global clientBufferSize
    serverReply = ''
    while True:
        data = sock.recv( clientBufferSize ).decode( )
        if not data:
            break
        serverReply += data
    return serverReply
        
sock = socket.socket( family = socket.AF_INET, type = socket.SOCK_STREAM )
sock.connect( serverInfo )
print( "connection to SERVER established" )
try:
    while True:
        msg = input( "Message To Server : " )
        if not msg:
            break
        print( 'Client Sending -> ' + msg )
        sock.send( msg.encode( ) )
        print( 'Server Replyed -> ' + GetServerReply( ) )
except Exception as e:
    print( e )
finally:
    print('closing socket')
    sock.close()
"""