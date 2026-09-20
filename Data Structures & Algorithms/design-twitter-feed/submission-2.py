class Twitter:

    def __init__(self):
        self.followers = defaultdict(list)
        self.user_tweets = defaultdict(list)
        self.global_time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time += 1
        self.user_tweets[userId].append([self.global_time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followers[userId]
        own_tweets = self.user_tweets[userId]
        followees_tweets = []
        for followee in followees:
            for tweet in self.user_tweets[followee]:
                followees_tweets.append(tweet)
        total_news_feed = followees_tweets + own_tweets
        
        news_feed = heapq.nlargest(10,total_news_feed)
        res = []
        for _,tweet in news_feed:
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

