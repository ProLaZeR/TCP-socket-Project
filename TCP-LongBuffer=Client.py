import socket
import threading

serverInfo = ( '127.0.0.1', 9999 )
clientBufferSize = 4096
sock = socket.socket( family = socket.AF_INET, type = socket.SOCK_STREAM ) # Internet; TCP
sock.connect( serverInfo )
print( 'connection to SERVER', serverInfo, 'established' )

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
