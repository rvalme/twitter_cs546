import numpy as np
class Artists:

        def __init__(self, artist_text):
            self.first_name = [tt].first_name
            self.last_name = [tt].last_name
            self.city = [tt].city
	    self.state = [tt].state
	    self.zip_code = [tt].zip_code
            self.id = np.random.randint(100000)
            self.artist_text = artist_text

        #def like_tweet(self, num_likes=1):
        #    self.num_likes = self.num_likes + num_likes

        #def add_comment(self, num_comments=1):
        #    self.num_comments = self.num_comments + num_comments

        #def add_retweet(self, num_retweets=1):
        #    self.num_retweets = self.num_retweets + num_retweets

        def print_artist(self):
            print("----------------------------------------------------------------------------------")
            print(self.artist_text)
            #print('Likes: ' + str(self.num_likes) + '       Retweets: ' + str(self.num_retweets) + '      Comments: ' + str(self.num_comments))
            print("----------------------------------------------------------------------------------")


class FindLocalArtist:
#find local artist

    def __init__(self, Artists, num_artists=10):
        self.num_artists = num_artists
        self.Artists = Artists
        self.filteredNF = {}


    def print_artist(self):
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
