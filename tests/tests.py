import sys
import unittest

sys.path.insert(0, "../bin/")
import config
import client
import decrypt

class wofs_testing(unittest.TestCase):
    def test_sha256(self):
	self.assertEqual(config.hash("goodPassword"),
			 "0747f7aecd1572460c3c90c0c75cbdde641b1039190ade8538b0ed0c559070df")

#    def test_createSocket(self):
#        self.assertEqual(client.createSocket(config.ip, config.port),
#			 socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((config.ip, config.port)))

    def test_decrypt(self):
	self.assertEqual(decrypt.decrypt("""-----BEGIN PGP MESSAGE-----

hQEMA8eIv1tKiID+AQf/fCLxQ9uw2MGl/bqixdzi0BW08yDjRKYSz9B6EcuERs8L
dSkcKVyOm00YJvm52RlBlYD3/2+pacb6XAb4BlZbiVHwzVRBF4f4Pc0zDUADphkj
YrUjIvahbeZSnPN320qY+3+viqbwiZ9mjsAwIr7ezr4VwodNqv/ghU8vZ6PmrABa
oo6K+DAJFh39amaNMio5EkhSiCcxj82LfaogHOWkbsEv6uW0S43fpjoIylzz4uv2
Ugm09d7BvszXECNrAE2jkXkJH0eSRoYX10an+n+e2Njt8o5xxwmKkKsrE+XrmTy/
BHtGOtKOzD6IjNQ4Z70Q0QiualKVKOL3lHrt0T/tBtI9AeKromdlkuoRMg803N3X
MawINL9XoKd+8FnGmewHXZMDRuVRR0G5u20cPp6vD03utsO1M2jgZthtEqIV/A==
=o6SW
-----END PGP MESSAGE-----
-------BEGIN PGP MESSAGE-----

hQEMA8eIv1tKiID+AQf/fhqc0TYx/3gR2SlZ4tl43xdo8DXhyzT1bGno/OpvEO1T
tlFXtEtLdKocMdKIK21RixPNomzs93/XO0ooCv101xiQYYELwmFvjtn+S0DE3njv
afY1j/QObqldxnUxpNfMWRGUTbebJsiSdUFwFH3/WvumF8gMFmRuruzgzK/6a/zF
swi6yyDU5IcJ/TXzhljcXyZ9+SPX+JhfiYD1nkMolttwim8YxhrXB7m0MmYJLLpx
MMrIZoVgdLxmpVVWpSavX3erO4WRaZUJZRunCfkWgDtRH6FIpRasEzgzoheJFQPw
l1rZS/WyjsznQd4nvZ+L3B9xnRVheVOsw8jIpkP3Z9I9Ab59QJxVQdBi9A+jz3DT
EKazLysjKYyGPbgToC3F5QRc5GFUchSlZbekefeUxdtG3861CgHjQumaIgpS6Q==
=dADC
-----END PGP MESSAGE-----
-----BEGIN PGP MESSAGE-----

hQEMA8eIv1tKiID+AQf9FuGx8yOq/21s8v4MoIl0H5Oo5XlKvUkW1TKIe6q/p0uF
Z0j+lHaNPTFrqUm3J+XmyUy3szoVUzHPlSd9c+scVY0U7fJxVWrH928qcJwTCkT4
dwS0B62Hk6PKUM97EjlbqtXSD7RlIPQT0WCxA/AImHlW53IWpugbyfzGBfKrTPkY
M7MoySmzpNr154dod6DAqC3+lanGrrIqOMuGmK8GKX1obCOxGMc59D4PmcAiSQWk
rZiyAAmBrmtxl4gar5GH/nmuxA1C9xetee7k7rPmprbosLdS6o9slJPAWNGk1pHn
E++uJY78KH/aVYqEEgNXjN2A3gcL6h08TiUfVYQqItI9ATglRzWhQ4YlrzVyy6x1
ZuCwaDbm5r3PhxoLLXr2rU452q+30SDNAuho7OrMm4tv0KR1zVeA1AU6g8Hl9w==
=mRvp
-----END PGP MESSAGE-----
"""), "ttt")

    def test_stripNewLinesFromStartAndEnd(self):
	self.assertEqual(decrypt.stripNewLinesFromStartAndEnd("\n\ntt\nt\n"), "tt\nt")

    def test_stripLinesAfterEnd(self):
	self.assertEqual(decrypt.stripLinesAfterEnd("g-----END PGP MESSAGE-----tttttt\ntttt"),
			 "g-----END PGP MESSAGE-----")

if __name__ == "__main__":
    unittest.main()
