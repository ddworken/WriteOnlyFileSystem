from hashlib import sha256

def hash(data):
    """ String -> String
	Returns the sha256 of the given data"""
    return sha256(data).hexdigest()

publicKey = "gpg.asc"  # filename of the GPG public key
chunkSize = 4096  # number of bytes sent over socket at a time
hashLength = 64  # Length of hash function in bytes
password = "superGoodPassword"  # Password used for authentication
ssl = False  # Enable or disable SSL
ip="0.0.0.0"  # IP of remote server
port=8080  # Port of remote server
