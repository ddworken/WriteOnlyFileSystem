import socket
import config
import ssl
from hashlib import sha256
from base64 import b64decode, b64encode

def isValid(data):
    """ String -> Boolean
	Returns whether the given data is properly authenticated"""
    if len(data) > 2*config.hashLength:
        hashed = config.hash(config.password)
        if data[:config.hashLength] == hashed:
            if data[-1*config.hashLength:] == hashed:
                return True

def processValidData(data):
    """ String -> None
	Takes valid authenticated data:
	    - Finds the filename
	    - Finds the data
	    - Writes the data to the filename"""
    filename = b64decode(data.split(':')[0])
    data = b64decode(data.split(':')[1])
    if ".." in filename or "/" in filename:
        print "No injection..."
        exit(1)
    print "Wrote data to " + filename
    with open("out/"+filename, 'w+') as f:
        f.write(data)

def getSocket():
    """ None -> Socket
	Returns a socket"""
    if config.ssl:
        _sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt = ssl.wrap_socket(_sckt, server_side=True, certfile="cert.crt", keyfile="cert.key")
        sckt.bind((config.ip, config.port))
        sckt.listen(10)
    else:
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.bind((config.ip, config.port))
        sckt.listen(10)
    return sckt

sckt = getSocket()

data = ""
while True:
    connection, address = sckt.accept()
    buf = connection.recv(config.chunkSize)
    if len(buf):
        data += buf
        if isValid(data):
            processValidData(data[config.hashLength:-1*config.hashLength])
            data = ""
