import numpy as np
class Tweet:

        def __init__(self, tweet_text):
            self.num_likes = 0
            self.num_comments = 0
            self.num_retweets = 0
            self.id = np.random.randint(100000)
            self.tweet_text = tweet_text

        def like_tweet(self, num_likes=1):
            self.num_likes = self.num_likes + num_likes

        def add_comment(self, num_comments=1):
            self.num_comments = self.num_comments + num_comments

        def add_retweet(self, num_retweets=1):
            self.num_retweets = self.num_retweets + num_retweets

        def print_tweet(self):
            print("----------------------------------------------------------------------------------")
            print(self.tweet_text)
            print('Likes: ' + str(self.num_likes) + '       Retweets: ' + str(self.num_retweets) + '      Comments: ' + str(self.num_comments))
            print("----------------------------------------------------------------------------------")


class NewsFeed:
#collection of 10 tweets

    def __init__(self, Tweets, num_tweets=10):
        self.num_tweets = num_tweets
        self.Tweets = Tweets
        self.filteredNF = {}


    def print_newsfeed(self):
        for x, ind in zip(self.Tweets, xrange(self.num_tweets)):
            self.Tweets[x].print_tweet()
            if ind == self.num_tweets:
                break

    def filter_newsfeed(self, topic):
        self.filteredNF = {}
        for x in self.Tweets:
            if topic in self.Tweets[x].tweet_text:
                self.filteredNF[x] = self.Tweets[x]


    def print_filtered_nf(self):
        for x in self.filteredNF:
            self.filteredNF[x].print_tweet()

class Artist:

        def __init__(self, artist):
            self.first_name = artist['first_name']
            self.last_name = artist['last_name']
            self.city = artist['city']
    	    self.state = artist['state']
    	    self.zip_code = artist['zip_code']
    	    self.bio = artist['bio']
    	    self.hobby = artist['topic']
            self.id = np.random.randint(100000)
            self.artist = artist
            self.dist = np.random.randint(10)


        def print_artist(self):
            print("------------------------------------------------------------------------------------------")
            print("   __")
            print("  ( ->")
            print("  / )\\")
            print(" <_/_/")
            print('  " "')

            print("| Name: "+ self.first_name + " " + self.last_name + " |")
            print("| Location: "+ self.city + "," + self.state + " |")
            print("| Bio: " + self.bio + " |")
            print("| Dist: " + str(self.dist) + "mi |")
            print("| Hobby: " + self.hobby + " |")
            print("------------------------------------------------------------------------------------------")


class LocalArtists:
#find local artist

    def __init__(self, Artists, num_artists=10):
        self.num_artists = num_artists
        self.Artists = Artists
        self.filteredNF = {}


    def print_artists(self):
        for x, ind in zip(self.Artists, xrange(self.num_artists)):
            self.Artists[x].print_artist()
            if ind == self.num_artists:
                break

    def filter_artist(self, topic):
        self.filteredNF = {}
        for x in self.Artists:
            if topic in self.Artists[x].artist_text:
                self.filteredNF[x] = self.Artists[x]


    def print_filtered_nf(self):
        for x in self.filteredNF:
            self.filteredNF[x].print_artist()
