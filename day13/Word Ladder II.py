from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return []

        words.discard(beginWord)
        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()

            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        candidate = word[:i] + ch + word[i + 1:]

                        if candidate in words:
                            next_level.add(candidate)
                            parents[candidate].append(word)

            words.difference_update(next_level)
            level = next_level

            if endWord in level:
                found = True

        result = []

        if found:
            path = [endWord]

            def build(word):
                if word == beginWord:
                    result.append(path[::-1])
                    return

                for prev in parents[word]:
                    path.append(prev)
                    build(prev)
                    path.pop()

            build(endWord)

        return result