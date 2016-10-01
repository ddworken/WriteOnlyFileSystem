import gnupg

class encryptor():
    def __init__(self, pubKey):
	self.pubKey = pubKey
	self.gpg = gnupg.GPG()
	self.gpg.import_keys(open(pubKey).read())
	self.fingerprint = self.gpg.list_keys()[0]['fingerprint']

    def encrypt(self, data):
	return str(self.gpg.encrypt(data, self.fingerprint))
