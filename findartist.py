import numpy as np
import json
from artist import Artist, FindLocalArtist
import csv
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
        tw = Artist(tt)
        #tw.like_tweet(np.random.randint(20))
        #tw.add_retweet(np.random.randint(20))
        #tw.add_comment(np.random.randint(20))
        tid.append(tw.id)
        Artists[tw.id] = tw
    Artistsf = FindLocalArtist(Artists)
    '''
    import pdb;pdb.set_trace()
    for tw in Tweets:
        Tweets[tw].print_tweet()
    '''
    #import pdb;pdb.set_trace()
    return Artistsf
    #Newsf.print_newsfeed()
#---------------------------------------




def start_loop(Artistsf):
#LOOP GUTS la - Print Local Artist, fl - Filter Local Artist by distance, e - End Session
#---------------------------------------
    inp = ''
    while(1):
        print("Find - Find Local Artist by distance, e End Session")
        inp = raw_input("Enter Zip Code: ")
        inp = inp.split(' ')
        if(inp[0] == 'Find'):

		zip_info_dct = {}
	with open('zipcodes.txt"', 'rb') as csvfile:
     		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     		for row in spamreader:
       			zip_code = row[4]
		first_name = row[0]
		last_name = row[1]		
		city = row[2]
		state = row[3]
		zip_info_dct [zip_code] = (city, state)
	zip_query = input("Enter a zip code to find (Press Enter key alone to stop): ")
	if zip_query in zip_info_dct : 
		info = zip_info_dct [zip_query]
		print "The city is %s and the state is %s" % (info [0], info [1])

    return search_result if search_result else None
    #Artistsf.print_localartist()

    #elif(inp[0] == 'e'):
    #        break
    #    elif('fl' in inp[0] and len(inp) == 2):
    #        Artistsf.filter_newsfeed(inp[1])
    #        Artistsf.print_filtered_nf()

if __name__ == "__main__":
    Artistsf = setup()
    start_loop(Artistsf)


