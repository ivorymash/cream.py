import random
import time
import json
import requests
from bs4 import BeautifulSoup

while True:
    def getDoujin():
        #random doujin
        code = random.randrange(314110)
        code = str(code)
        page = "http://nhentai.net/g/" + code
        return page


    def filters():
        #gw memek let this disease pass on from this world.
        #first two tags are chinese and japanese
        badtags = ["29963", "6346" , "29013", "23895", "21712", "2820", "12523", "30645", "5529", "35970", "73750", "35968", "27217", "10542", "32602", "35971", "24933", "16236", "5200", "22221", "36957", "15425", "32282", "2956", "779", "6343", "5529", "706", "27217", "14069", "10542", "7354", "4549", "21924", "30848", "13057", "15959", "25996", "29347", "2695", "28335", "23183", "19479"]

        for i in range (0, len(badtags)): #badtag filtering
            if soup.find_all("a", {'class' :'tag tag-' + badtags[i]}):
                print('BAD TAG')
                flag = False
                return flag
                #FINDS A BAD TAG
            flag = True #If no bad tags are found, return flag true and breaks loop
        return flag

    def tweet():
        requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update",
        json={"api_key":"OMITTED","status":"Automated nHentai connoisseur with python version 2: " + soup.find('h1').text.strip() + " " + html})





    illegalCheck = False

    while(not illegalCheck):
        html = getDoujin()
        page = requests.get(html)
        soup = BeautifulSoup(page.content, 'html.parser')
        illegalCheck = filters()
        print(illegalCheck)
        print(soup.find('h1').text.strip())
    print('ITS FUCKING LEGAL ' + html)

    print('LETS FUCKING GOOOO TWEETING TIME')
    tweet()
    time.sleep(300)
