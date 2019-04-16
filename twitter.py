import numpy as np
import json
from tweet import Tweet, NewsFeed
import random
import time

def setup():
#LOOP SETUP
#---------------------------------------
    with open("cs_546.json") as json_file:
        tweet_texts = json.load(json_file)

    Tweets = {}
    tid = []
    for _ in xrange(100): #tweet_texts['tweets']:
        tt = random.choice(tweet_texts['tweets'])
        tw = Tweet(tt)
        tw.like_tweet(np.random.randint(20))
        tw.add_retweet(np.random.randint(20))
        tw.add_comment(np.random.randint(20))
        tid.append(tw.id)
        Tweets[tw.id] = tw
    Newsf = NewsFeed(Tweets)
    '''
    import pdb;pdb.set_trace()
    for tw in Tweets:
        Tweets[tw].print_tweet()
    '''
    return Newsf
    #Newsf.print_newsfeed()
#---------------------------------------




def start_loop(Newsf):
#LOOP GUTS pn - Print News Feed, fn - Filter News Feed, - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("pn - Print News Feed, fn topic - Filter NewsFeed, e End Session")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'pn'):
            Newsf.print_newsfeed()
        elif(inp[0] == 'e'):
            break
        elif('fn' in inp[0] and len(inp) == 2):
            Newsf.filter_newsfeed(inp[1])
            Newsf.print_filtered_nf()

if __name__ == "__main__":
    Newsf = setup()
    start_loop(Newsf)


