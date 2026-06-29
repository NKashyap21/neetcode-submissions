class Twitter:

    def __init__(self):
        self.following = {} #userId : set()        
        self.tweets = {} #userId: set((timestamp,tweet))
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].add((self.time,tweetId))
        else:
            self.tweets[userId] = {(self.time,tweetId)}
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        for timestamp,tweet in self.tweets.get(userId,[]):
            all_tweets.append((timestamp,tweet))
        for followee in self.following.get(userId,[]):
            for timestamp,tweet in self.tweets.get(followee,[]):
                all_tweets.append((timestamp,tweet))
        
        heap = all_tweets[:10]
        heapq.heapify(heap)

        for timestamp,tweet in all_tweets[10:]:
            if timestamp > heap[0][0]:
                heapq.heapreplace(heap,(timestamp,tweet))
        
        res = []
        while heap:
            _,tweet = heapq.heappop(heap)
            res.append(tweet)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return 
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
    
