from typing import List
from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # Store positions of every character in word1
        positions = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            positions[ord(ch) - ord('a')].append(i)

        # latest[j] = latest possible index to start matching
        # word2[j:] exactly
        latest = [-1] * (m + 1)
        latest[m] = n

        limit = n

        for j in range(m - 1, -1, -1):
            arr = positions[ord(word2[j]) - ord('a')]
            p = bisect_left(arr, limit) - 1

            if p < 0:
                limit = -1
            else:
                limit = arr[p]

            latest[j] = limit

        # prev_diff[i] = latest index before i whose character
        # is different from word1[i]
        prev_diff = [-1] * n

        last_pos = -1
        last_char = -1
        second_pos = -1
        second_char = -1

        for i, ch in enumerate(word1):
            c = ord(ch) - ord('a')

            if last_char != c:
                prev_diff[i] = last_pos
            else:
                prev_diff[i] = second_pos

            if last_char == c:
                last_pos = i
            else:
                second_pos = last_pos
                second_char = last_char
                last_pos = i
                last_char = c

        # best[j] = latest possible first index for word2[j:]
        # when at most one character is allowed to be different
        best = [-1] * (m + 1)
        best[m] = n

        for j in range(m - 1, -1, -1):
            target = ord(word2[j]) - ord('a')
            candidate = -1

            # Use an exact match at this position.
            limit = best[j + 1]

            if limit >= 0:
                arr = positions[target]
                p = bisect_left(arr, limit) - 1

                if p >= 0:
                    candidate = arr[p]

            # Use the one allowed mismatch at this position.
            limit = latest[j + 1]

            if limit > 0:
                i = limit - 1

                if word1[i] != word2[j]:
                    mismatch_pos = i
                else:
                    mismatch_pos = prev_diff[i]

                if mismatch_pos > candidate:
                    candidate = mismatch_pos

            best[j] = candidate

        # Greedily choose the smallest possible index at every position.
        answer = []
        prev = -1
        mismatch_used = False

        for j in range(m):
            i = prev + 1

            while i < n:
                same = word1[i] == word2[j]

                if mismatch_used:
                    # No mismatch left, so this character must match.
                    if same and i < latest[j + 1]:
                        answer.append(i)
                        prev = i
                        break

                else:
                    if same:
                        # We can either keep the mismatch for later
                        # or finish using the remaining suffix.
                        if i < best[j + 1]:
                            answer.append(i)
                            prev = i
                            break
                    else:
                        # Use our one allowed mismatch here.
                        if i < latest[j + 1]:
                            answer.append(i)
                            prev = i
                            mismatch_used = True
                            break

                i += 1

            else:
                return []

        return answer