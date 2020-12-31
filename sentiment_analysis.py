from fetch_twitter_data import TwitterGrabber


def main():
    api = TwitterGrabber()
    print("What key word would you like me to analyse")
    while True:
        try:
            query = str(input())
            break
        except Exception:
            print("Invalid input, try again or q to quit")
    tweets = api.get_tweets(query=query, count=200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    f = open("sentiment_analysis_result.txt", "w", encoding="utf-8")
    print("Positive tweets percentage: {} %".format(
        100*len(ptweets)/len(tweets)))
    f.write("Positive tweets percentage: {} %\n".format(
        100*len(ptweets)/len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Negative tweets percentage: {} %".format(
        100*len(ntweets)/len(tweets)))
    f.write("Negative tweets percentage: {} %\n".format(
        100*len(ntweets)/len(tweets)))
    print("Neutral tweets percentage: {} %".format(
        100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    f.write("Neutral tweets percentage: {} %\n".format(
        100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    print("\nPositive tweets:")
    f.write("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
        f.write('\n' + str(tweet['text']))
    print("\n\nNegative tweets:")
    f.write("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
        f.write('\n' + str(tweet['text']))
    f.close()


if __name__ == "__main__":
    main()
