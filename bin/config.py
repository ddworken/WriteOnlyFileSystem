from hashlib import sha256

def hash(data):
    """ String -> String
	Returns the sha256 of the given data"""
    return sha256(data).hexdigest()

publicKey = "gpg.asc"  # filename of the GPG public key
chunkSize = 32768  # number of bytes sent over socket at a time
hashLength = 64  # Length of hash function in bytes
password = "superGoodPassword123"  # Password used for authentication
ssl = False  # Enable or disable SSL
ip="45.55.154.94"  # IP of remote server
port=8080  # Port of remote server
