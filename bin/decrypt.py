from sys import argv
import config
import gnupg
from subprocess import check_output
import os

def decrypt(data):
    gpg = gnupg.GPG()
    gpgChunks = [str for str in data.split("-----BEGIN PGP MESSAGE-----")[1:]]
    decrypted = ""
    for chunk in gpgChunks:
	chunk = "-----BEGIN PGP MESSAGE-----" + chunk
	chunk = stripNewLinesFromStartAndEnd(stripLinesAfterEnd(chunk))
	with open('/tmp/temp.gpg', 'w+') as f:
	    f.write(chunk)
	with open(os.devnull, 'w') as dn:
	    decrypted += check_output('gpg --decrypt /tmp/temp.gpg', shell=True, stderr=dn)[:-1]
    return decrypted

def stripNewLinesFromStartAndEnd(string):
    return string.lstrip().rstrip()

def stripLinesAfterEnd(string):
    return string.split("-----END PGP MESSAGE-----")[0]+"-----END PGP MESSAGE-----"

if __name__ == "__main__":
    print decrypt(open(argv[1]).read())
