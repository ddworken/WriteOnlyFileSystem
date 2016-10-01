from hashlib import sha256

def hash(data):
    return sha256(data).hexdigest()

publicKey = "gpg.asc"
chunkSize = 4
hashLength = 64
password = "superGoodPassword"
ssl = False
ip="0.0.0.0"
port=8080
