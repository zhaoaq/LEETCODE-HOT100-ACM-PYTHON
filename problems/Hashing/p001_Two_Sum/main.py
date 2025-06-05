#Python中的字典本质是对哈希表的高级封装。字典是键值对，一般用键找值。所以我们把元素值设为键，索引设为值。就可以通过字典的特性由元素值查找对应的索引。
#enumerate() 函数，它能同时遍历列表的索引和元素值：
# i：当前元素的索引（位置）。
# num：当前元素的值。
# nums：输入的整数列表。
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #花括号就是初始化字典
        for i, value in enumerate(nums):
            complement = target - value #定义“补数”
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[value] = i #通过键赋值（list的索引在字典里是值）
        return []


target = int(input().strip())

#map(func, iterable) 是 Python 的内置函数，它会将函数 function 应用到可迭代对象 iterable 的每一个元素上，并返回一个迭代器（iterator）
#map(int, ["2", "7", "11", "15"]) 返回一个迭代器，逐个生成整数 2, 7, 11, 15

#输入nums第一种格式: 2 7 11 15
#nums = list(map(int, input().split()))

#输入nums第二种格式: [2,7,11,15]
line = input().strip()
nums = list(map(int, line[1:-1].split(',')))

sulotion = Solution()
print(sulotion.twoSum(nums, target))



