from time import time
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # userId -> set of users they follow
        self.follows = defaultdict(set)

        # monotonically increasing value for global tweet sorting
        self.postCount = 0

        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postCount += 1
        post = (-self.postCount, tweetId)
        self.tweets[userId].append(post)

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        for followee in self.follows[userId]:
            minHeap.extend(self.tweets[followee])

        minHeap.extend(self.tweets[userId])
        heapq.heapify(minHeap)
            
        res = []

        while minHeap and len(res) < 10:
            _, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

        return res

    # Add the followeeId to the user's followed set
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        
    # Remove the followeeId from the user's followed set
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
