# WriteOnlyFileSystem

WriteOnlyFileSystem or WOFS is a FUSE based python program to create a cryptographically backed secure write only file system with automatic one way backup of logs to an external server. 

## Usage

1. Run ```python wofs.py /mnt``` to mount a cryptographically backed write only filesystem in ```/mnt/```. 
2. Run ```python server.py``` on a remote server to create a secure SSL authenticated server to host encrypted backups of the logs. 
3. When you need to view the contents of ```log.txt``` run ```python decrypt.py log.txt```to view the plaintext log file. 

## Installation

1. ```git clone https://github.com/ddworken/WriteOnlyFileSystem.git```
2. ```cd WriteOnlyFileSystem```
3. ```pip install -r requirements.txt```
4. Ensure you have a GPG public key in your GPG keychain
5. Ensure you don't have the matching GPG private key in your GPG keychain
