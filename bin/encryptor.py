import gnupg

class encryptor():
    def __init__(self, pubKey):
	""" String -> None
	    pubKey is the filename of the GPG public key"""
	self.pubKey = pubKey
	self.gpg = gnupg.GPG()
	self.gpg.import_keys(open(pubKey).read())
	self.fingerprint = self.gpg.list_keys()[1]['fingerprint']

    def encrypt(self, data):
	""" String -> String
	    Encrypts the given data with the public key"""
	return str(self.gpg.encrypt(data, self.fingerprint)).replace("-----BEGIN PGP MESSAGE-----", "").replace("-----END PGP MESSAGE-----","").lstrip().rstrip()+"\n\n"
