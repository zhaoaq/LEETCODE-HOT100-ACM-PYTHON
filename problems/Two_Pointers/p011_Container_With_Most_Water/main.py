from typing import List

class Solution:
    def maxArea(self, height: List[int]):
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[right], height[left])
            if left >= right:
                right -= 1
            else:
                left += 1
            res = max(res, area)

        return res

#输入格式：1,8,6,2,5,4,8,3,7
height = list (map(int, input().split(",")))
#输入格式：[1,8,6,2,5,4,8,3,7]
#height = list(map(int, input().strip('[] ').split(',')))
#print(height)

soluton = Solution()
print(soluton.maxArea(height))