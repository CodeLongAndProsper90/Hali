from time import sleep
import sys
from random import uniform

def type(text, time=1):
    i=0
    while i < time:
        for x in text:
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(0, 0.1))  # random sleep from 0 to 0.3 seconds
        print('\n')
        sleep(0.50)
        i=i+1
def tinput(prompt):
        for x in prompt:
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(0, 0.1))  # random sleep from 0 to 0.3 seconds
        ans = input(' ')
        return ans
def setup():
    type("Welcome to the Halibut setup tool!")
    type('Loading... ',time=3)
    type('You may be wondering why your install has stopped.')
    type('It is because Halibut uses a configuration file. This tool will help you set one up.')
    start = tinput('Ready?')
    if start.lower() == 'yes':
        type("OK!")
        page = tinput("What is the EXACT web address you want to set your home page to? [In the form http(s)://address.domain]")
        last = page
        to_write = f'home: {page}\nlast: {last}'
        config = open('config','w')
        config.write(to_write)
        config.close()
        del to_write, page, last
        type('We now return you to your regulary scheduled install.')
    else:
        abort = tinput('SIGNAL ABORT. Do you want to stop?')
        if abort.lower() == 'yes' or 'y':
            exit()
        else:
            setup()
setup()

