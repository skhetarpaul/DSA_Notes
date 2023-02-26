# https://leetcode.com/problems/minimize-deviation-in-array/submissions/904122319/
'''Note the key concept, we cannot deal with odds and even together, so it is important to bring them on the same page.
It is better to convert odd to even since odd*2 will be an even number anyways, which will further termiate any more operations.
Further, is it really treuiqired to maintain 2 heaps?
Can we not deal with a single heap, give a thought?

Treemap is a concept, where we somehow need to capture minimum and maximum in  O(1) time.'''

import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        max_heap = []
        for num in nums:
            if num % 2 == 0:
                num = -num
            
            else:
                num = -num * 2

            heapq.heappush(max_heap, num)

        
        min_dev = float('inf')
        min_val = -max(max_heap)

        while len(nums) == len(max_heap):
            curr = -heapq.heappop(max_heap)
            min_dev = min(min_dev, curr- min_val)
            if curr % 2 == 0:
                min_val = min(min_val, curr//2)
                heapq.heappush(max_heap, -curr//2)
            else:
                break
        
        return min_dev