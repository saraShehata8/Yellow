# import pyfiglet module
from pyfiglet import Figlet
import os
from time import sleep 

f = Figlet(font='slant')
logo= f.renderText('YELLOW')

sleep(1)

print(logo)
sleep(1)

print('Connectting to the Server... ')
print('\n\n')

os.system('curl -s https://otx.alienvault.com/api/v1/pulses/subscribed?page=1 -H "X-OTX-API-KEY: 31e82c7fbc820fd472d43a3fd4e5d7b8b759dfcb1730ba2e328b1db68b743890" | jq "."')