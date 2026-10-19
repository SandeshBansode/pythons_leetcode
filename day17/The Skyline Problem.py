import heapq

class Solution:
    def getSkyline(self, buildings):
        starts = {}
        xs = set()

        for left, right, height in buildings:
            xs.add(left)
            xs.add(right)
            starts.setdefault(left, []).append((height, right))

        heap = [(0, float("inf"))]
        result = []

        for x in sorted(xs):
            for height, right in starts.get(x, []):
                heapq.heappush(heap, (-height, right))

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            current = -heap[0][0]

            if not result or result[-1][1] != current:
                result.append([x, current])

        return result