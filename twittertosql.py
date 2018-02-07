import sys
import tweepy
import webbrowser
import sqlite3 as lite
import csv

# Query terms

#Q = sys.argv[1:]

sqlite3file=''

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

con = lite.connect('hello.db')
cur = con.cursor()   

#cur.execute(" CREATE TABLE TWEETS1(txt varchar, author varchar, created varchar, source varchar)")

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):

       try:
            print "%s\n%s\n%s\n%s\n" % (status.text, 
                                      status.author.screen_name, 
                                      status.author.location, 
                                      status.source)
                                      
            with open('result3_tweets.csv', 'a') as acsv:
                w = csv.writer(acsv)
                #w.writerow(('Status', 'Tweet', 'id', 'source'))
                w.writerow((status.text, status.author.screen_name, status.author.location, status.source))
            
            
           # cur.execute("insert into TWEETS1 values (1,22,333,44)", status.text)
           # cur.execute("INSERT INTO TWEETS1 VALUES (?,?,?,?)"
           # , (status.text, 
                                                            #status.author.screen_name, 
                                                         # status.created_at, 
                                                           # status.source))
       except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['...'])
#streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

#print >> sys.stderr, 'Filtering the public timeline for "%s"' % (' '.join(sys.argv[1:]),)

#streaming_api.filter(follow=None, track=Q)
