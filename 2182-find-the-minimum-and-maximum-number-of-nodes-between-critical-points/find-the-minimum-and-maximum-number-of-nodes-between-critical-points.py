class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next is not None:
            nxt = curr.next

            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = nxt
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]