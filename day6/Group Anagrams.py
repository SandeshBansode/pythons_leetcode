class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            key = tuple(sorted(set(s)))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
    