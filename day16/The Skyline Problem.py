class Solution:
    def getSkyline(self, buildings):
        events = []

        for left, right, height in buildings:
            events.append((left, 0, height, right))
            events.append((right, 1, height, right))

        events.sort()
        active = []
        result = []
        previous = 0

        for x, kind, height, right in events:
            if kind == 0:
                active.append((height, right))
            else:
                active.remove((height, right))

            current = max(
                (h for h, end in active if end > x),
                default=0
            )

            if current != previous:
                result.append([x, current])
                previous = current

        return result