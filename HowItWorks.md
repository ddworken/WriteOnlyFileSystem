# Summary

At a high level, WOFS works via using FUSEpy to override the write file function so that it encrypts the data and backs it up remotely. 

# Encryption

All encryption is asymmetric encryption done via GPG. When a program writes to a file in the WOFS mounted filesystem, the following pseudocode executes:

```
define write(path, data):
    encrypted = gpgEncrypt(data)
    file[path] += encrypted
    sendFile(remoteServer, file[path])
```

This means that the on disk format of an encrypted file is a series of GPG encrypted appends. This is because it impossible to directly store the encrypted file without decrypting it—which would defeat the purpose of the WOFS. 

# Remote Backup

The remote backup function works via authenticated SSL wrapped sockets. Authentication is completed via sha256(password). The SSL certificate for the sockets is pinned to ensure that a MITM attack is impossible. This ensures that an attacker cannot obtain the password needed to backup logs to the server. 
