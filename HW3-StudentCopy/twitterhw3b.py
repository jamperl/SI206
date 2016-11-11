# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

access_token = "229230573-nQpNQMT9uG9zsejH6vXHdtUZDihmm3FmlgccWrSb"
access_token_secret = "UUkCnSaFk0wGSNS6iWpSq7YUpDeL8ELAmfKcCfQdq6aO6"
consumer_key = "Pvh61VmA4uqEpfRoXPX7YHrfU"
consumer_secret = "PiGoD87ITrCrMm0aqv9GOClNLsOOFRv9j8YooUmSdHTbvStSGv"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

pol_sum = 0 # total for polarity
subj_sum = 0 # total for subjectivity
count = 0 # counter for total tweets collected

tweet_group = api.search("Toronto Maple Leafs")

print ("***TWEETS***")
for tweet in tweet_group:
	blob = TextBlob(tweet.text) #use tweepy to format tweets
	print (blob)
	sent = blob.sentiment # collect sentiment
	polarity = sent.polarity
	subjectivity = sent.subjectivity
	pol_sum += polarity # add polarity value to total
	subj_sum += subjectivity # add subjectivity value to total
	count += 1 # add one tweet to the count
print ("\n***SENTIMENT***")
print("Average subjectivity is", round((subj_sum/count), 2)) # complete computation of averages
print("Average polarity is", round((pol_sum/count), 2))
