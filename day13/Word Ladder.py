from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        words.discard(beginWord)

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    candidate = word[:i] + ch + word[i + 1:]

                    if candidate in words:
                        words.remove(candidate)
                        queue.append((candidate, length + 1))

        return 0