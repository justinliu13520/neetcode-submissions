class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.global_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time -= 1
        self.user_tweets[userId].append([self.global_time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = self.followees[userId].union({userId})
        latest_tweets = []
        for candidate in candidates:
            num_of_tweets = len(self.user_tweets[candidate])
            if num_of_tweets:
                latest_tweet = self.user_tweets[candidate][-1]
                latest_tweet_time = latest_tweet[0]
                latest_tweets.append([latest_tweet_time,latest_tweet[1],num_of_tweets-1,candidate])
        res = []
        heapq.heapify(latest_tweets)
        while latest_tweets and len(res) < 10:
            _,tweet,idx,uid = heapq.heappop(latest_tweets)
            res.append(tweet)
            if idx - 1 >= 0:
                time = self.user_tweets[uid][idx-1][0]
                tweet = self.user_tweets[uid][idx-1][1]
                heapq.heappush(latest_tweets,[time,tweet,idx-1,uid])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followees[followerId]:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
