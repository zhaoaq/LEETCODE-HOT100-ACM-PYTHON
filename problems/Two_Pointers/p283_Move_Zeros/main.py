#语法糖：python中交换两个元组可以直接用nums[l], nums[r] = nums[r], nums[l]。避免了tmp中间变量的使用
class Solution:
    def moveZeros(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

#输入格式：0,1,0,3,12
nums = list(map(int, input().split(",")))

#输入格式：[0,1,0,3,12]
#nums = list(map(int, input()[1:-1].split(",")))
#print(nums)

solution = Solution()
solution.moveZeros(nums)
print(nums)