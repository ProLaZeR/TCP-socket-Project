import socket
import threading

serverInfo = ( '127.0.0.1', 9999 )    # Local Host; Port 9999
serverBuffer = 4096
sock = socket.socket( family = socket.AF_INET, type = socket.SOCK_STREAM ) # Internet; TCP
sock.bind( serverInfo )
sock.listen( 5 )
print( '********************\nReady to accept a client connection request' )






"""""
try:
    while True:
        connection, clientInfo = sock.accept( )
        print( 'Got connection from', clientInfo )
        while True:
            data = connection.recv( serverBuffer ).decode( )
            if not data:
                print( 'Client', clientInfo, 'disconnected .....' )
                break
            else:
                print( 'message received from', clientInfo, ': ' + data )
                connection.send( 'Got it'.encode( ) )
except Exception as e:
    print( e )



try:
    while True:
        connection, clientInfo = sock.accept( )
        print( 'clientInfo=', clientInfo )
        try:
            while True:
                data = connection.recv( serverBuffer ).decode( )
                if not data:
                    print( 'Client', clientInfo, 'disconnected .....' )
                    break
                else:
                    print( 'message received from', clientInfo, ': ' + data )
                    #connection.send( ( 'Reply from', serverInfo, 'echo -> ' + data ).encode( ) ) 
                    connection.send( 'Got it'.encode( ) )
        except:
            print( 'exception 1' )
except:
    print( 'exception 2' )
"""
'''
The socket.bind() method in Python is used to to bind a SERVER to a specific IP address and a port.

The socket.listen() method in Python is used to enable a SERVER to accept incoming connections. 
It is called on a socket object after the socket.bind() method. 
The basic syntax is socket.listen([backlog]), where backlog specifies the maximum number of queued connections. 
If not specified, a default reasonable value is chosen by the system. 
'''