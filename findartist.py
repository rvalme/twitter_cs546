import numpy as np
import json
from artist import Artists, FindLocalArtist
import random
import time

def setup():
#LOOP SETUP
#---------------------------------------
    with open("artist.json") as json_file:
        artist_texts = json.load(json_file)

    Artists = {}
    tid = []
    for _ in range(100): #tweet_texts['tweets']:
        tt = random.choice(artist_texts["artists"])
        tw = Artists[tt]
        #tw.like_tweet(np.random.randint(20))
        #tw.add_retweet(np.random.randint(20))
        #tw.add_comment(np.random.randint(20))
        tid.append(tw.id)
        Artists[tw.id] = tw
    Artistsf = ArtistFeed(Artists)
    '''
    import pdb;pdb.set_trace()
    for tw in Tweets:
        Tweets[tw].print_tweet()
    '''
    return Artistf
    #Newsf.print_newsfeed()
#---------------------------------------




def start_loop(Newsf):
#LOOP GUTS la - Print Local Artist, fl - Filter Local Artist by distance, e - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("la - Print Local Artist, fl - Filter Local Artist by distance, e End Session")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'la'):
            Artistsf.print_localartist()
        elif(inp[0] == 'e'):
            break
        elif('fl' in inp[0] and len(inp) == 2):
            Artistsf.filter_newsfeed(inp[1])
            Artistsf.print_filtered_nf()

if __name__ == "__main__":
    Artistsf = setup()
    start_loop(Artistsf)


