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
        self.filteredNF = {}


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
