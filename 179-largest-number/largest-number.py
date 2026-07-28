from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings
        arr = []
        for num in nums:
            arr.append(str(num))

        # Custom comparison
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        arr.sort(key=cmp_to_key(compare))

        answer = ""
        for num in arr:
            answer += num

        # Handle cases like [0,0]
        if answer[0] == "0":
            return "0"

        return answer