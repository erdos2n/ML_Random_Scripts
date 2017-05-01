#Stores 100 tweets
import csv
import tweepy
from textblob import TextBlob

consumer_key = '-'
consumer_secret = '-'

access_token = '---'
access_secret = '-'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepyapi = tweepy.API(auth)

public_tweets = api.search('Rick and Morty')
count = 1
#create csv file

csvFile = open('RickandMorty.csv', 'a')
csvWriter = csv.writer(csvFile)
count2 = 0
while count <= 10000:
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		count += 1
		#print(tweet.text.encode('utf-8'))
		# if analysis.polarity > 0:
			# print(tweet.text.encode('utf-8'))
			# print(analysis.sentiment)

		#if analysis.sentiment.subjectivity >= 0.4:
			# print(count, analysis.sentiment)
		sentval = analysis.sentiment[0]
		if sentval < 0:
			lbl = "negative"
		elif sentval == 0:
			lbl = "neutral"
		else:
			lbl = "positive"
		row = [lbl,'-',[tweet.text.encode('utf-8'), analysis.sentiment[0], analysis.sentiment[1]]]
		
		csvWriter.writerow(row)

csvFile.close()
