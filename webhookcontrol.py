from dhooks import Webhook
import termcolor
url = Webhook(input(termcolor.colored('[#] Enter Webhook URL: ', 'blue')))
while True:
 message = input(termcolor.colored('[#] Enter Message: ', 'blue'))
 url.send(message)
 print(termcolor.colored('[+] Message Successfully Sent', 'green'))
 print(termcolor.colored(('[*] Message: ' + message), 'yellow'))
