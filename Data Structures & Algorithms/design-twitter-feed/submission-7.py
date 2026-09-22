from _heapq import heappush
class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.global_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time -= 1
        self.user_tweets[userId].append([self.global_time,tweetId])
        print([self.global_time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        potential_tweeters = self.followees[userId].union({userId})
        news_heap = []
        for potential_tweeter in potential_tweeters:
            if self.user_tweets[potential_tweeter]:
                last_idx = len(self.user_tweets[potential_tweeter]) - 1
                tweet_time = self.user_tweets[potential_tweeter][-1][0]
                tweet_id = self.user_tweets[potential_tweeter][-1][1]
                heapq.heappush(news_heap,(tweet_time,tweet_id,potential_tweeter,last_idx))
        res = []
        while news_heap and len(res) < 10:
            time,tweet_id,uid,idx = heapq.heappop(news_heap)
            res.append(tweet_id)
            if idx - 1 >= 0:
                followees_tweets = self.user_tweets[uid]
                next_recent_tweet_time = followees_tweets[idx - 1][0]
                next_tweet_id = followees_tweets[idx - 1][1]
                heapq.heappush(news_heap,(next_recent_tweet_time,next_tweet_id,uid,idx-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
