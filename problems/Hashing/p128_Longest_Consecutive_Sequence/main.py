# 最长连续序列（Longest Consecutive Sequence） 是指由连续整数组成的最长子序列，该子序列中的元素可以不连续出现于原数组中，
# 但必须严格递增且相邻元素之间的差值为 1。因此要用set对原数据进行去重
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for x in nums_set:
            # x - 1不在，说明x是开头的
            if (x - 1) not in nums_set:
                #易错点：不要忘记把第一个计数
                length = 1
                while (x + 1) in nums_set:
                    length += 1
                    x += 1
                longest = max(length, longest)

        return longest

#输入格式1：100 4 200 1 3 2
nums = list(map(int, input().split()))
# input返回字符串类型的，所以记住要转成int。
# split()方法默认按照多个连续空白字符分割

#输入格式2：[0,3,7,2,5,8,4,6,0,1]
# nums = list(map(int, input()[1:-1].split(",")))
# print(nums)

solution = Solution()
print(solution.longestConsecutive(nums))
