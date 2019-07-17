import tweepy
import time

print("This is my twitter bot")

CONSUMER_KEY = 'wQdwnV4hlou92s6dfTpk9MbRt'
CONSUMER_SECRET = '4vt3ZskEQ4DrdKa2wAVZ151xVzLehUqDLf2yuqMfsVzsTA1fIZ'
ACCESS_KEY = '1149738047124193280-M98EiJ1yKMWRuZoywaFMZ1hNqJiAOJ'
ACCESS_SECRET = 'tZ8KMaKd0eGQXndZX33D5auVKvT0mln9umEE6cgcri5g1'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
# We are going to be using this api object to 
# basically talk to Twitter and read/write data into Twitter

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # Note: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        api.create_favorite(mention.id)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

