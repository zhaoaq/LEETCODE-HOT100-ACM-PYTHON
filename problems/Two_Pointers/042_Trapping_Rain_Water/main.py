#关键思路\公式：每个位置所装雨水 = min（它左边最高的，它右边最高的）- 该位置本身高度
from typing import List

class Solution:
    def trap(self,height:List[int]):
        res = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            #易错点：在循环里记得更新两边分别的最大值
            left_max = max(left_max,height[left])
            right_max = max(right_max, height[right])
            #谁小的话，那侧就可以安全地算res，因此就用那个索引处的max和height【】
            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res

height = list(map(int, input().split(",")))
#print(height)

solution = Solution()
print(solution.trap(height))