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
    print(" _    _      _                            _____")
    print("| |  | |    | |                          |_   _|")
    print("| |  | | ___| | ___ ___  _ __ ___   ___    | | ___")
    print("| |/\\| |/ _ \ |/ __/ _ \\| '_ ` _ \\ / _ \   | |/ _ \\")
    print("\\  /\\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |")
    print(" \\/  \\/ \___|_|\\___\\___/|_| |_| |_|\\___|   \\_/\\___/")
    print("")
    print("")
    print("  _____        _ _   _                               ")
    print(" |_   _|      (_) | | |           _                  ")
    print("   | |_      ___| |_| |_ ___ _ __(_)                 ")
    print("   | \\ \\ /\\ / / | __| __/ _ \\ '__|                   ")
    print("   | |\\ V  V /| | |_| ||  __/ |   _")
    print("   \\_/ \\_/\\_/ |_|\\__|\\__\\___|_|  (_)")


    while(1):
        #print("pn - Print NewsFeed, lt - List Topics fn topic - Filter NewsFeed,  li id - Like Tweet, re id - Retweet, cm id - Comment, lh - List Hobbies,  ph - Print Hobbyists, fh hobby - Filter Hobbyists by hobby, fd dist - Filter Hobbyist by distance in mi, e - End Session")
        print("##################################################################################")
        print("----------------------------------USAGE-------------------------------------------")
        print("##################################################################################")
        print("1. pn - Print NewsFeed")
        print("2. lt - List Topics")
        print("3. fn topic - Filter NewsFeed")
        print("4. li id - Like Tweet")
        print("5. re id - Retweet Tweet")
        print("6. cm id - Comment on Tweet")
        print("7. lh - List Hobbies")
        print("8. ph - Print Hobbyists")
        print("9. fh hobby - Filter Hobbyists by hobby")
        print("10. fd distance - Filter Hobbyists by distance in mi. Max distance is 10 mi.")
        print("11. e - End session")
        inp = raw_input("Enter: ")
        inp = inp.split(' ')
        if(inp[0] == 'ph' or inp[0] == '8'):
            LocalArtists.print_artists()
        elif(inp[0] == 'pn' or inp[0] == '1'):
            Newsf.print_newsfeed(tid)
        elif(inp[0] == 'lt' or inp[0] == '2'):
            Newsf.print_topics()
        elif(inp[0] == 'lh' or inp[0] == '7'):
            LocalArtists.print_hobbies()
        elif(inp[0] == 'e' or inp[0] == '11'):
            break
        elif(('fn' in inp[0] or '3' in inp[0])  and len(inp) == 2):
            Newsf.filter_newsfeed(inp[1])
            Newsf.print_filtered_nf()
        elif(('fh' in inp[0] or '9' in inp[0]) and len(inp) == 2):
            LocalArtists.filter_hobbies(inp[1])
            LocalArtists.print_filtered_artists()
        elif(('fd' in inp[0] or '10'in inp[0]) and len(inp) == 2):
            LocalArtists.filter_distance(inp[1])
            LocalArtists.print_filtered_artists()
        elif(len(inp) == 2):
            try:
                twid = int(inp[1])
                if twid not in tid:
                    print('Tweet does not exist')
                elif('li' in inp[0] or '4' in inp[0]):
                    Newsf.Tweets[twid].like_tweet()
                elif('re' in inp[0] or '5' in inp[0]):
                    Newsf.Tweets[twid].add_retweet()
                elif('cm' in inp[0] or '6' in inp[0]):
                    Newsf.Tweets[twid].add_comment()
            except:
                print('ID is not a number')


if __name__ == "__main__":
    Newsf, tid, LocalArtists = setup()
    start_loop(Newsf, tid, LocalArtists)


