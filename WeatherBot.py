import requests
import datetime
import tweepy
from Keys import consumer_key, consumer_secret, access_token, access_secret

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    url = "https://api.darksky.net/forecast/1b344af14054572a62de555a58e4bf7d/35.090328, -92.441559"
    data = requests.get(url).json()
    weekday = getWeekday(data)
    date = getDate(data)
    if weekday == "Monday":
        weeklySummary = getWeeklySummary(data)
        mondayMessage = writeMondayMessage(date, weekday, weeklySummary)
        tweet(mondayMessage)
        print(mondayMessage)
    low_temp = getLowTemp(data)
    high_temp = getHighTemp(data)
    dailySummary = getSummary(data)
    dailyMessage = writeMessage(date, weekday, dailySummary, low_temp, high_temp)
    tweet(dailyMessage)
    print(dailyMessage)

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

def writeMondayMessage(date, weekday, weeklySummary):
    return("Today is " + weekday + ", " + str(date) \
    + ". " + weeklySummary)

def writeMessage(date, weekday, summary, low_temp, high_temp):
    return("Today is " + weekday + ", " + str(date) \
    + ". The high for today is " + str(high_temp) \
    + ", and the low is " + str(low_temp) + ". " \
    + summary)

main()
