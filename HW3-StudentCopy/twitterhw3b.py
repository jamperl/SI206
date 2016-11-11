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

pol_sum = 0
pol_count = 0
subj_sum = 0
subj_count = 0

tweet_group = api.search("Toronto Maple Leafs")

print ("***TWEETS***")
for tweet in tweet_group:
	blob = TextBlob(tweet.text)
	print (blob)
	sent = blob.sentiment
	polarity = sent.polarity
	subjectivity = sent.subjectivity
	pol_sum += polarity
	pol_count += 1
	subj_sum += subjectivity
	subj_count += 1
print ("\n***SENTIMENT***")
print("Average subjectivity is", round((subj_sum/subj_count), 2))
print("Average polarity is", round((pol_sum/pol_count), 2))
