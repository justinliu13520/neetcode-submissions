class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.global_time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time -= 1
        self.user_tweets[userId].append((self.global_time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        user_followees = self.followees[userId]
        tweets = []
        for followee in user_followees:
            for tweet in self.user_tweets[followee]:
                tweets.append(tweet)
        tweets += self.user_tweets[userId]
        heapq.heapify(tweets)
        res = []
        while tweets:
            if len(res) == 10:
                break
            res.append(heapq.heappop(tweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:    
            self.followees[followerId].remove(followeeId)
