import  twitter
from pprint import pprint as pp

consumer_key= "your Key"
consumer_secret ='your Key'
accsess_token="your Key"
accsess_secret="your Key"

my_auth=twitter.oauth.OAuth(accsess_token, accsess_secret, consumer_key, consumer_secret)

api=twitter.Twitter(auth=my_auth)

def Tweets(q):
    search_results=api.search.tweets(q=q ,count=10,)
    statuses = search_results['statuses']
    for x in statuses:
     person=x['entities']
     print(person)
     print(x['text'])
     print("  ")

#      statuses=search_results['statuses']
# user=(statuses[0])
#
# username=(user['entities'])
# print(username['user_mentions'][0]['screen_name'])
#
# # print(username['screen_name'])

Tweets("sderot")