from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #defaultdict(list) 是 Python 标准库 collections 中的一个特殊字典类型，它的作用是当访问不存在的键时，
        # 自动创建一个默认值（这里是一个空列表），从而避免了普通字典可能引发的 KeyError 异常。
        res = defaultdict(list)
        # s是“eat”
        for s in strs:
            key = "".join(sorted(s)) #"".join()字符串连接起来，以空字符串连接
            res[key].append(s) #在建后面加上值

        return list(res.values()) #dict.values()展示所有值

#split() 方法用于将字符串按指定分隔符分割成多个子字符串，并返回一个列表（list）。注意返回的不是数组。
#["eat","tea","tan","ate","nat","bat"]
line = input().strip()
strs = list(line[2:-2].split("\",\""))

#print(strs) #检查输入格式是否正确
solution = Solution()
print(solution.groupAnagrams(strs))