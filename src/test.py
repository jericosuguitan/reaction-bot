# From dotenv import load_dotenv
# load_dotenv()

import os
val = os.environ.get('BOT_TOKEN')

if val is not None:
    print('token = ' + val)
else:
    print("RIP THE DREAM bc val")

    # i can write in basic python woooo

###

print("test number 2")

os.environ['USER'] = 'RAY'
name = os.environ.get('USER')

if name is not None:
    print('his name is ' + name)
else:
    print("you tried XD")

###

print("test number 3")

os.environ['NUMBER'] = '34+35'
number = os.environ['NUMBER']

if number is not None:
    print('ariana grande and her hit single is ' + number)
else:
    print('ya really tried bruh')

###

print("test number 4")

symbol = os.environ["PREFIX"]
print(type(symbol))

if number is not None:
    print('hit em with that ' + symbol)
else:
    print('A for effort bro')