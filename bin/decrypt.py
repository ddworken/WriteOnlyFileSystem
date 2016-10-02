from sys import argv
import config
import gnupg
from subprocess import check_output
import os

def decrypt(data):
    """ String -> String
	Takes a string that is a series of armored GPG encrypted strings.
	Returns the decrypted output of all of thsoe concatenated together."""
    gpg = gnupg.GPG()
    gpgChunks = [str for str in data.split("\n\n")[:-1]]
    decrypted = ""
    for chunk in gpgChunks:
	chunk = "-----BEGIN PGP MESSAGE-----\n\n" + chunk + "\n-----END PGP MESSAGE-----\n"
	with open('/tmp/temp.gpg', 'w+') as f:
	    f.write(chunk)
	with open(os.devnull, 'w') as dn:
	    # dirty hack but the GPG library is horrible
	    decrypted += check_output('gpg --decrypt /tmp/temp.gpg', shell=True, stderr=dn)[:-1]
    return decrypted

def stripNewLinesFromStartAndEnd(string):
    """ String -> String
	Strips whitespace from the start and end of a string"""
    return string.lstrip().rstrip()

def stripLinesAfterEnd(string):
    """ String -> String
	Strips any lines after the end of a PGP message"""
    return string.split("-----END PGP MESSAGE-----")[0]+"-----END PGP MESSAGE-----"

if __name__ == "__main__":
    print decrypt(open(argv[1]).read())
