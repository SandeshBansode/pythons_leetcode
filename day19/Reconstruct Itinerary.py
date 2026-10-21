import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        stack = ["JFK"]
        route = []

        while stack:
            airport = stack[-1]

            if graph[airport]:
                stack.append(heapq.heappop(graph[airport]))
            else:
                route.append(stack.pop())

        return route[::-1]