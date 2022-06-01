from tkinter import messagebox as msgbox
import termcolor
from colorama import Fore
print(f'{Fore.LIGHTCYAN_EX}##############################\n#          Icon list:        #\n##############################\n\n[1] Error\n\n[2] Warning\n\n[3] Info\n')
while True:
    titlein = input(termcolor.colored('[#] Enter Title: ', 'blue'))
    textin = input(termcolor.colored('[#] Enter Text: ', 'blue'))
    iconin = input(termcolor.colored('[#] Enter Icon Number: ', 'blue'))
    if iconin == '1':
        msgbox.showerror(titlein, textin)
    if iconin == '2':
        msgbox.showwarning(titlein, textin)
    if iconin == '3':
        msgbox.showinfo(titlein, textin)