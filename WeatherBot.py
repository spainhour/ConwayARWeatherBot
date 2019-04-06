import requests
import datetime
import tweepy
from Keys import *

def main():
    url = "https://api.darksky.net/forecast/1b344af14054572a62de555a58e4bf7d/35.090328, -92.441559"
    data = requests.get(url).json()
    date = getDate()
    low_temp = getLowTemp()
    high_temp = getHighTemp()
    message = writeMessage(date, low_temp, high_temp)
#    tweet(message)
    print(message)

def tweet(message):
    account = tweepy.OAuthHandler(consumer_key, consumer_secret)
    account.set_access_token(access_token, access_secret)
    bot = tweepy.API(account)
    bot.update_status(message)

def getLowTemp():
    return(int(data['daily']['data'][0]['temperatureMin']))

def getHighTemp():
    return(int(data['daily']['data'][0]['temperatureMax']))

def getDate():
    date = data['daily']['data'][0]['time']
    date = str(datetime.datetime.fromtimestamp(date))
    return date

def writeMessage(date, high_temp, low_temp):
    message = "Today is " + str(date) + ". The High for today is " + str(high_temp) + ", and the Low is " + str(low_temp) + "."

main()
