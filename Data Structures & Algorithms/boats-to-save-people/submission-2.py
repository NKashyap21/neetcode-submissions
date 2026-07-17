class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        count = 0
        while l < r:
            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            elif people[r] <= limit:
                count += 1
                r -= 1
        if l == r and people[l] <= limit:
            count += 1
        return count 
