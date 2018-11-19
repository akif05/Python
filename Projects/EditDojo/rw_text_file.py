import tweepy
import time

print('This is my twitter bot')
CONSUMER_KEY = 'kljewqojro3j1'
CONSUMER_SECRET = 'AADFafafasdg'
ACCESS_KEY = 'adfgadfgadfgadfgadf'
ACCESS_SECRET = 'asdgasgfdsghAAAgahdfh'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

## Test mentions #################################
## Delete after test, at he end of the progam s actual code we will use
##################################################
#mentions = api.mentions_timeline()
#for mentoion in mentions:
#    print(str(mention.id) + ' - ' + mention.text)
#    if '#helloworkld' in mention.text.lower():
#        print('Found #helloworld')
#        print('Responding back ...')
## End of mentions test #########################

FILE_NAME = 'last_seen_id.txt'

def retrive_last_seen_id(file_name):
    with open(file_name, 'r') as f:
        last_seen_id = int(f.read().strip())
        return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    with open(file_name, 'w') as f:
        f.write(str(last_seen_id))
        return 

### For testing file read write ############
# print (retrive_last_seen_id(FILE_NAME))  #
# store_last_seen_id(111111111, FILE_NAME) #
# print (retrive_last_seen_id(FILE_NAME))  #
############################################

#for mention in reversed(mentions);
#    print(str(mention.id) + ' - ' + mention.full_text)
#    last_seen_id = mention.id
#    store_last_seen_id(last_seen_id, FILE_NAME)
#    if '#helloworld' in mention.full_text.lower():
#        print('found #helloworld!')
        print('respond back: ')
        api.update_status('@' + mention.user.screen_name +
                '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

