import requests
import datetime
import tweepy
from Keys import *

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    inputQuestion = input("Tweet the weather forecast? y/n ")
    if inputQuestion == "y":
        url = "https://api.darksky.net/forecast/1b344af14054572a62de555a58e4bf7d/35.090328, -92.441559"
        data = requests.get(url).json()
        weekday = getWeekday(data)
        if weekday == "Monday":
            date = getDate(data)
            weeklySummary = getWeeklySummary(data)
            message = writeMessage(date, weekday, weeklySummary, None, None, None)
        else:
            date = getDate(data)
            low_temp = getLowTemp(data)
            high_temp = getHighTemp(data)
            dailySummary = getSummary(data)
            message = writeMessage(date, weekday, dailySummary, low_temp, high_temp)
#       tweet(message)
        print(message)

def tweet(message):
    account = tweepy.OAuthHandler(consumer_key, consumer_secret)
    account.set_access_token(access_token, access_secret)
    bot = tweepy.API(account)
    bot.update_status(message)

def getWeeklySummary(data):
    return(data['daily']['summary'])

def getSummary(data):
    return(data['daily']['data'][0]['summary'])

def getPrecipProb(data):
    return(int(data['daily']['data'][0]['precipProbability'])*100)

def getLowTemp(data):
    return(int(data['daily']['data'][0]['temperatureMin']))

def getHighTemp(data):
    return(int(data['daily']['data'][0]['temperatureMax']))

def getWeekday(data):
    date = data['currently']['time']
    weekday = datetime.date.fromtimestamp(date).weekday()
    weekday = daysOfWeek[weekday]
    return weekday

def getDate(data):
    date = data['currently']['time']
    date = str(datetime.date.fromtimestamp(date))
    return date

def writeMessage(date, weekday, summary, low_temp=None, high_temp=None, precip_probability=None):
    if weekday == "Monday":
        return("Today is " + weekday + ", " + str(date) \
        + ". " + summary)
    else:
        return("Today is " + weekday + ", " + str(date) \
        + ". The high for today is " + str(high_temp) \
        + ", and the low is " + str(low_temp) + "." \
        + summary)

main()
