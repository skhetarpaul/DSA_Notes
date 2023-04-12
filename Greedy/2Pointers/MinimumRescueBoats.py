# https://leetcode.com/problems/boats-to-save-people/description/
'''Intuition behind using 2 pointer approach:
A certain game of maxima/minima and we can at max use 2 people only. This closely relates to a 2 pointer game'''


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people)-1
        boats = 0
        while i<=j:
            if people[i] + people[j]<=limit:
                i+=1
                j-=1
                boats+=1
            else:
                boats+=1
                j-=1
        return boats

                