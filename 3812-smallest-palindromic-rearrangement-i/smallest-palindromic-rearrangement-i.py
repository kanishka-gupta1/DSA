from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        first_half = ""
        middle = ""

        for ch in sorted(count):
            times = count[ch] // 2
            first_half += ch * times

            if count[ch] % 2 == 1:
                middle = ch

        second_half = first_half[::-1]

        return first_half + middle + second_half