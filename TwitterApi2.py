import  twitter
from pprint import pprint as pp

#-----------------------------------------------------------------------------
# This example will show how to use Python lib twitter
# Twitter Api see who have mentioned my Username
# and Reply to all those posts
#-----------------------------------------------------------------------------


# User needs to create key at using his Twitter account
# and put this data in below strings

consumer_key= "your Key"
consumer_secret ='your Key'
accsess_token="your Key"
accsess_secret="your Key"

#function to create twitter using twitter lib

my_auth=twitter.oauth.OAuth(accsess_token, accsess_secret, consumer_key, consumer_secret)

api=twitter.Twitter(auth=my_auth)

#Search for tweets by keywork insert

def Tweets(q):
    search_results=api.search.tweets(q=q ,count=10,)
    statuses = search_results['statuses']
    for x in statuses:
     person=x['entities']
     print(person)
     print(x['text'])
     print("  ")



Tweets("sderot")