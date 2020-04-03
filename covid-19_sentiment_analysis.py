import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = '-'
consumer_secret = '-'
access_token = '-'
access_token_secret = '-'
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Failed to connect to API")

def tweet_filter(tweet):
    cleantweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split());
    cleantweet =  cleantweet.replace('\n',' ')
    
    return cleantweet;

def tweet_sentiment(tweet):
    analysis = TextBlob(tweet_filter(tweet))
     
    if analysis.sentiment.polarity > 0:
        print("positive")
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        print("neutral")
        return 'neutral'
    else:
        print("negative")
        return 'negative'

tweets = []
query = "COVID-19"
count = 200

try:
    tweetcount = 0
    tweets = []
    query = "Coronavirus"
    count = 200
    fetch_tweets = api.search(query, count=200)
    
    for tweet in fetch_tweets:
        tweetcount += 1
        clean_tweets = {}
        text_tweet= tweet.text
        print(text_tweet)
        print("-----------------------------------")
        clean_tweets['text'] = text_tweet
        clean_tweets['sentiment'] = tweet_sentiment(tweet.text)
        if tweet.retweet_count > 0:
            if clean_tweets not in tweets:
                tweets.append(clean_tweets)
        else:
            tweets.append(clean_tweets)

    positive_tweets = [tweet for tweet in tweets if tweet['sentiment']=='positive']
    neutral_tweets = [tweet for tweet in tweets if tweet['sentiment']=='neutral']
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment']=='negative']
    results = open("covid_sentiment_analysis", "w", encoding="utf-8")
    
    positive_tweets_percentage = 0
    neutral_tweets_percentage = 0 
    negative_tweets_percentage = 0
    
    if len(positive_tweets) > 0:
        positive_tweets_percentage = len(positive_tweets)/len(tweets)*100
    if len(neutral_tweets) > 0:    
        neutral_tweets_percentage = len(neutral_tweets)/len(tweets)*100
    if len(negative_tweets) > 0:    
        negative_tweets_percentage = len(negative_tweets)/len(tweets)*100

    print("Positive tweets percentage : {}% \n".format(positive_tweets_percentage))
    print("Neutral tweets percentage : {}% \n".format(neutral_tweets_percentage))
    print("Negative tweets percentage : {}% \n".format(negative_tweets_percentage))
    
    print("number of tweets is {}".format(tweetcount))
    
    results = open("covid_sentiment_analysis.txt", "w")
    results.write("Positive tweets about covid-19 percentage : {}% \n".format(positive_tweets_percentage))
    results.write("Neutral tweets covid-19 percentage : {}% \n".format(neutral_tweets_percentage))
    results.write("Negative tweets covid-19 percentage : {}% \n".format(negative_tweets_percentage))

except tweepy.TweepError as e:
    print("Error : " + str(e))



    
    
