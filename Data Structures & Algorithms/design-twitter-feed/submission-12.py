from _heapq import heapify
class Twitter:

    def __init__(self):
        self.followee = defaultdict(set)
        self.user_post = defaultdict(list)
        self.global_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time -= 1
        self.user_post[userId].append([self.global_time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        users_followees = self.followee[userId] | {userId}
        heap = []
        res = []
        for potential_tweeter in users_followees:
            if self.user_post[potential_tweeter]:
                last_idx = len(self.user_post[potential_tweeter]) - 1
                tweet_time = self.user_post[potential_tweeter][-1][0]
                tweet_id = self.user_post[potential_tweeter][-1][1]
                heapq.heappush(heap,(tweet_time,tweet_id,potential_tweeter,last_idx))
        while len(res) < 10 and heap:
            _,tweet_id,uid,idx = heapq.heappop(heap)
            res.append(tweet_id)
            if idx - 1 >= 0:
                followees_tweets = self.user_post[uid]
                next_recent_tweet_time = followees_tweets[idx - 1][0]
                next_tweet_id = followees_tweets[idx - 1][1]
                heapq.heappush(heap,(next_recent_tweet_time,next_tweet_id,uid,idx-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)
