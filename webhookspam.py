from dhooks import Webhook
import termcolor
from termcolor import colored
url_hook = Webhook(input(termcolor.colored('[#] Enter Webhook URL: ', 'blue')))
msg = input(termcolor.colored('[#] Enter Message: ','blue'))
while True:
    url_hook.send(msg)
    print(termcolor.colored('[+] Message Successfully Sent', 'green'))
    print(termcolor.colored(('[*] Message: ' + msg), 'yellow'))
