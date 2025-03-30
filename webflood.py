#FloodPhishingSite
#A script that can be used to flood a phishing website with useless information.
#This script is designed confuse the Phishing Website makers, flooding them with useless information.
#Warning: Recommend use with a proxy.
#How to use it?
#Inspect the phishing website to find out the form elements (email, password). Then change the data structure in the attack function. #Also update the url with the phsihing website's url.
#Then launch it with:
#python3 webflood.py 5
#(replace 5 with the number of threads you want to launch)
 
import urllib
import urllib2
import random
import string
from threading import Thread
import sys
import time
import socket
import requests

'''the number of threads'''
num = int(sys.argv[1])

'''the number of minutes to run'''
minute = int(sys.argv[2])

'''the time to stop'''
timeout = time.time() + 60*minute

def attack():
    while True:
        if time.time() <= timeout:
            data = {
                'email': id_generator(random.randint(3,10))+"@"+id_generator(random.randint(3,10))+".com",
                'password': id_generator(random.randint(3,10)),
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for _ in range(4))
            }
            req = urllib2.Request(url="",
                                  data=urllib.urlencode(data),
                                  headers=headers)
            response = urllib2.urlopen(req)
            the_page = response.read()
            print('flooded with ' + str(data))
        else:
            break

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    for k in range(0, num):
        thread = Thread(target=attack)
        thread.start()
        print('Launched thread ' + str(k))
        print()
