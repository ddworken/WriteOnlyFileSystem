import socket
import config
from base64 import b64decode, b64encode
from sys import argv
import ssl

def createSocket(ip, port):
    """ String, Number -> Socket
	Returns a socket connected to the given IP and port"""
    if config.ssl:
        _sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt = ssl.wrap_socket(_sckt, ca_certs='cert.crt', cert_reqs=ssl.CERT_REQUIRED)
        sckt.connect((ip, port))
    else:
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.connect((ip, port))
    return sckt

def sendData(ip, port, data, password, chunkSize=4096):
    """ String, Number, String, String -> None
	Send's the given data over a socket to a remote server at ip,port.
	Authenticates with the given password."""
    hashed = config.hash(config.password)
    data = hashed+data+hashed
    for i in range(0, len(data), chunkSize):
        createSocket(ip, port).send(data[i:i+chunkSize])

def createFile(ip, port, filename, data, password, chunkSize=4096):
    """ String, NUmber, String, String, String -> None
	Create's a file with filename and data on the remote server
	using password to authenticate."""
    encodedData = b64encode(filename)+":"+b64encode(data)
    sendData(ip, port, encodedData, password, chunkSize=chunkSize)

if __name__ == "__main__":
    if len(argv)  == 1:
        print "Usage: python client.py filename file_data"

    if len(argv) == 3:
        createFile('localhost',
                   8080,
                   argv[1],
                   argv[2],
                   config.password,
                   chunkSize=4)
    else:
        if len(argv) == 2:
            with open(argv[1]) as f:
                data = f.read()
            createFile('localhost',
                       8080,
                       argv[1],
                       data,
                       config.password,
                       chunkSize=config.chunkSize)

