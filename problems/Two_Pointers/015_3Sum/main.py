# 灵神双指针法
# 1. 先排序（因为要求输出的是元素值而不是下标，所以下标乱了无所谓）
# 2. 排序以后。第0个元素是i，第一个元素是left，最后一个元素是right
# 3. s = nums[i]+nums[left]+nums[right]，s为三数之和
# 如果s > 0，说明当前三数之和大了，将right指针向左移动，尝试减小和的值。
# 如果s < 0，说明当前三数之和小了，将left指针向右移动，尝试增大和的值。
# 如果s == 0，说明找到了一组满足条件的三元组，将这三个元素值组成的列表添加到result数组中，
# 然后通过内层的两个while循环跳过left和right指针指向的重复元素，接着继续移动left和right指针去寻找下一组可能的解。

# 核心是防止得到重复的，所以在for和while之间，s = 0内部都有去重的操作

# 初始化一个名字为列表的方法，很简单 ，= []
# 排序 .sort()
from typing import List

class Solution:
    def threeSum(self,nums:List[int]):
        #不要忘记排序
        nums.sort()
        n = len(nums)
        i = 0
        res = []

        for i in range(n - 2):
            # 第一次去重，0的判断是防止数组溢出
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #每次左右指针都要更新
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    #第二次去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #同时移动左右指针
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return res

nums = list(map(int, input().split(",")))
#print(nums)
solution = Solution()
print(solution.threeSum(nums))
