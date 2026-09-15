class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        # pal[i] stores palindrome starts ending at i
        pal = [[] for _ in range(n)]

        for center in range(n):
            # Odd length palindromes
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pal[r].append(l)
                l -= 1
                r += 1

            # Even length palindromes
            l = center
            r = center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pal[r].append(l)
                l -= 1
                r += 1

        for i in range(n):
            dp[i + 1] = dp[i]

            for start in pal[i]:
                dp[i + 1] = max(dp[i + 1], dp[start] + 1)

        return dp[n]