import socket
import config
from base64 import b64decode, b64encode
from sys import argv
import ssl

def createSocket(ip, port):
    if config.ssl:
        _sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt = ssl.wrap_socket(_sckt, ca_certs='cert.crt', cert_reqs=ssl.CERT_REQUIRED)
        sckt.connect((ip, port))
    else:
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.connect((ip, port))
    return sckt

def sendData(ip, port, data, password, chunkSize=4096):
    hashed = config.hash(config.password)
    data = hashed+data+hashed
    for i in range(0, len(data), chunkSize):
        createSocket(ip, port).send(data[i:i+chunkSize])

def createFile(ip, port, filename, data, password, chunkSize=4096):
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

