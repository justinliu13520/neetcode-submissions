class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.global_time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_time -= 1
        self.user_tweets[userId].append((self.global_time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = self.followees[userId] | {userId}
        heap = []
        
        # STEP 1: seed the heap with each user's most recent tweet
        for uid in candidates:
            tweets = self.user_tweets[uid]
            if tweets:
                idx = len(tweets) - 1        # last index = most recent (list is oldest -> newest)
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (time, tweetId, uid, idx))

        res = []
        while heap and len(res) < 10:
            # STEP 2: pop the current most-recent tweet across all candidates
            time, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            # STEP 3: pull in that SAME user's next-most-recent tweet, if any
            if idx - 1 >= 0:
                prev_time, prev_tweetId = self.user_tweets[uid][idx - 1]
                heapq.heappush(heap, (prev_time, prev_tweetId, uid, idx - 1))
            # if idx - 1 < 0, that user has no more tweets -- nothing to push, list is exhausted

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:    
            self.followees[followerId].remove(followeeId)
