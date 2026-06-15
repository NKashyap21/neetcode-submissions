class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []#idx,h

        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx,h = stack.pop()
                maxArea = max(maxArea,h*(i-idx))
                start = idx
            stack.append([start,height])
        
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))
        return maxArea