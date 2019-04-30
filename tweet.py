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
            print('Tweet id: ' + str(self.id))
            print("----------------------------------------------------------------------------------")


class NewsFeed:
#collection of 10 tweets

    def __init__(self, Tweets, num_tweets=10):
        self.num_tweets = num_tweets
        self.FeedPosition = 0
        self.FeedMax = 100
        self.Tweets = Tweets
        self.topics = ['music', 'art', 'money', 'entertainment', 'media', 'science', 'history', 'math', 'news']
        self.filteredNF = {}


    def print_topics(self):
        print("##################################################################################")
        print("----------------------------------TOPICS------------------------------------------")
        print("##################################################################################")
        for ind, x in enumerate(self.topics):
            print(str(ind + 1) + '. ' + x)

    def print_newsfeed(self, tid):
        print("##################################################################################")
        print("----------------------------------NEWSFEED----------------------------------------")
        print("##################################################################################")
        for x, ind in zip(tid, xrange(self.num_tweets)):
            self.Tweets[tid[self.FeedPosition]].print_tweet()
            self.FeedPosition += 1
            if ind >= self.num_tweets:
                break
        if(self.FeedPosition >= self.FeedMax):
            self.FeedPosition = 0


    def filter_newsfeed(self, topic):
        self.filteredNF = {}
        for x in self.Tweets:
            if topic in self.Tweets[x].tweet_text:
                self.filteredNF[x] = self.Tweets[x]


    def print_filtered_nf(self):
        print("##################################################################################")
        print("-----------------------------FILTERED-NEWSFEED------------------------------------")
        print("##################################################################################")
        for x in self.filteredNF:
            self.filteredNF[x].print_tweet()

class Artist:

        def __init__(self, artist):
            self.first_name = artist['first_name']
            self.last_name = artist['last_name']
            self.city = artist['city']
    	    self.state = artist['state']
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
            print("| Bio: " + self.bio + " |")
            print("| Dist: " + str(self.dist) + "mi |")
            print("| Hobby: " + self.hobby + " |")
            print("------------------------------------------------------------------------------------------")


class LocalArtists:
#find local artist

    def __init__(self, Artists, num_artists=10):
        self.num_artists = num_artists
        self.Artists = Artists
        self.hobbies = ['music', 'painting', 'calligraphy', 'graphic design', 'sculpting', 'drawing']
        self.filteredArtists = {}


    def print_hobbies(self):
        print("##################################################################################")
        print("----------------------------------HOBBIES-----------------------------------------")
        print("##################################################################################")
        for ind, x in enumerate(self.hobbies):
            print(str(ind + 1) + '. ' + x)

    def print_artists(self):
        print("##################################################################################")
        print("---------------------------------HOBBIESTS----------------------------------------")
        print("##################################################################################")
        for x, ind in zip(self.Artists, xrange(self.num_artists)):
            self.Artists[x].print_artist()
            if ind == self.num_artists:
                break

    def filter_hobbies(self, topic):
        print("##################################################################################")
        print("-----------------------------FILTERED HOBBIESTS-----------------------------------")
        print("##################################################################################")
        self.filteredArtists = {}
        for x in self.Artists:
            if topic == self.Artists[x].hobby:
                self.filteredArtists[x] = self.Artists[x]

    def filter_distance(self, topic):
        self.filteredArtists = {}
        for x in self.Artists:
            if self.Artists[x].dist < int(topic):
                self.filteredArtists[x] = self.Artists[x]



    def print_filtered_artists(self):
        for x in self.filteredArtists:
            self.filteredArtists[x].print_artist()
