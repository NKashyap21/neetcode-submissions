class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -float('inf')

        start,end = 0 ,len(heights)-1
        while start < end:
            area = min(heights[start],heights[end]) * (end-start)
            max_area = max(area,max_area)

            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1

        return int(max_area)