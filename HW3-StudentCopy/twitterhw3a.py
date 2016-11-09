# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

access_token = "229230573-nQpNQMT9uG9zsejH6vXHdtUZDihmm3FmlgccWrSb"
access_token_secret = "UUkCnSaFk0wGSNS6iWpSq7YUpDeL8ELAmfKcCfQdq6aO6"
consumer_key = "Pvh61VmA4uqEpfRoXPX7YHrfU"
consumer_secret = "PiGoD87ITrCrMm0aqv9GOClNLsOOFRv9j8YooUmSdHTbvStSGv"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

img = 'leafs.png'
txt = "#UMSI-206 #Proj3"
api.update_with_media(img, status=txt)