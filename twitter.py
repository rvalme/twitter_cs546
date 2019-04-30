import numpy as np
import json
from tweet import Tweet, NewsFeed, Artist, LocalArtists
import random
import time

def setup():
#LOOP SETUP
#---------------------------------------
    with open("cs_546.json") as json_file:
        tweet_texts = json.load(json_file)

    with open("artist.json") as json_file:
        artists = json.load(json_file)

    Tweets = {}
    Artists = {}
    tid = []
    aid = []
    max_artists = len(artists['artists'])
    for x in xrange(max_artists):
        rn = np.random.randint(max_artists - x) #always will be a unique artist
        ard = artists['artists'][rn]
        artists['artists'].pop(rn)
        ar = Artist(ard)
        aid.append(ar.id)
        Artists[ar.id] = ar
    LocalA = LocalArtists(Artists)

    max_tweets = len(tweet_texts['tweets'])
    for x in xrange(max_tweets):
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
    return (Newsf, tid, LocalA)
    #Newsf.print_newsfeed()
#---------------------------------------



def start_loop(Newsf, tid, LocalArtists):
#LOOP GUTS pn - Print News Feed, fn - Filter News Feed,  l id - Like Tweet, re id - Retweet, c id - Comment, e - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("pn - Print NewsFeed, fn topic - Filter NewsFeed,  li id - Like Tweet, re id - Retweet, cm id - Comment, ph = Print Hobbyists, e - End Session")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'ph'):
            LocalArtists.print_artists()
        elif(inp[0] == 'pn'):
            Newsf.print_newsfeed(tid)
        elif(inp[0] == 'e'):
            break
        elif('fn' in inp[0] and len(inp) == 2):
            Newsf.filter_newsfeed(inp[1])
            Newsf.print_filtered_nf()
        elif(len(inp) == 2):
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
    Newsf, tid, LocalArtists = setup()
    start_loop(Newsf, tid, LocalArtists)


