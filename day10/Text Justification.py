class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - letters

            if j == n or count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                slots = count - 1
                gap = spaces // slots
                extra = spaces % slots
                parts = []

                for k in range(slots):
                    parts.append(words[i + k])
                    parts.append(" " * (gap + (1 if k < extra else 0)))

                parts.append(words[j - 1])
                line = "".join(parts)

            result.append(line)
            i = j

        return result