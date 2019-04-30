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
    for _ in xrange(18):
        ard = random.choice(artists['artists'])
        ar = Artist(ard)
        aid.append(ar.id)
        Artists[ar.id] = ar
    LocalA = LocalArtists(Artists)

    for _ in xrange(100): #tweet_texts['tweets']:
        tt = random.choice(tweet_texts['tweets'])
        tw = Tweet(tt)
        tw.like_tweet(np.random.randint(20))
        tw.add_retweet(np.random.randint(20))
        tw.add_comment(np.random.randint(20))
        tid.append(tw.id)
        Tweets[tw.id] = tw
    Newsf = NewsFeed(Tweets)
    return (Newsf,LocalA)
#---------------------------------------




def start_loop(Newsf, LocalArtists):
#LOOP GUTS pn - Print News Feed, fn - Filter News Feed, - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("pn - Print News Feed, fn topic - Filter NewsFeed, e End Session, pa - Print Artists")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'pa'):
            LocalArtists.print_artists()
        if(inp[0] == 'pn'):
            Newsf.print_newsfeed()
        elif(inp[0] == 'e'):
            break
        elif('fn' in inp[0] and len(inp) == 2):
            Newsf.filter_newsfeed(inp[1])
            Newsf.print_filtered_nf()

if __name__ == "__main__":
    Newsf, LocalArtists = setup()
    start_loop(Newsf, LocalArtists)


