from ftplib import FTP

#domain name or server ip:
HOST = "192.168.1.204"
PORT = 3721

ftp = FTP()
ftp.connect(host=HOST,port=PORT)
ftp.cwd('/VidMate/downloads/')

#ftp.login(user='username', passwd = 'password')
