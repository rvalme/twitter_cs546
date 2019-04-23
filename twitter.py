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
    max_tweets = len(tweet_texts['tweets'])
    for x in xrange(max_tweets): #tweet_texts['tweets']:
        rn = np.random.randint(max_tweets - x) #always will be a unique tweet
        tt = tweet_texts['tweets'][rn]
        tweet_texts['tweets'].pop(rn)
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
    return (Newsf, tid)
    #Newsf.print_newsfeed()
#---------------------------------------




def start_loop(Newsf, tid):
#LOOP GUTS pn - Print News Feed, fn - Filter News Feed,  l id - Like Tweet, re id - Retweet, c id - Comment, e - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("pn - Print NewsFeed, fn topic - Filter NewsFeed,  li id - Like Tweet, re id - Retweet, cm id - Comment, e - End Session")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'pn'):
            Newsf.print_newsfeed(tid)
        elif(inp[0] == 'e'):
            break
        elif('fn' in inp[0] and len(inp) == 2):
            Newsf.filter_newsfeed(inp[1])
            Newsf.print_filtered_nf()
        try:
            twid = int(inp[1])
            if twid not in tid:
                print('Tweet does not exist')
            elif('li' in inp[0] and len(inp) == 2):
                Newsf.Tweets[twid].like_tweet()
            elif('re' in inp[0] and len(inp) == 2):
                Newsf.Tweets[twid].add_retweet()
            elif('cm' in inp[0] and len(inp) == 2):
                Newsf.Tweets[twid].add_comment()
        except:
            print('ID is not a number')


if __name__ == "__main__":
    Newsf,tid = setup()
    start_loop(Newsf, tid)


