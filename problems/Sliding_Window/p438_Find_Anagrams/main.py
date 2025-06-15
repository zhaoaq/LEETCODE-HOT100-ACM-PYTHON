# from collections import Counter
# # 统计字符串中各字符的出现次数
# s = "hello world"
# char_counter = Counter(s)
# print(char_counter)
# # 输出：Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
from collections import Counter

#注意切片左闭右开

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        s_len = len(s)
        p_len = len(p)

        #剪枝
        if s_len < p_len:
            return res

        #创建窗口用Counter（）返回字典
        p_counter = Counter(p)
        window = Counter(s[:p_len - 1])

        for i in range(p_len - 1, s_len):
            #右侧的频率 + 1
            window[s[i]] += 1

            if window == p_counter:
                res.append(i - p_len + 1)

            #左侧频率 - 1
            window[s[i - p_len + 1]] -= 1
            #左侧频率为0 移除左侧
            if window[s[i - p_len + 1]] == 0:
                #注意字典键的移除语法
                del window[s[i - p_len + 1]]

        return res

s = input()
p = input()

# print(s)
# print(p)

solution = Solution()
print(solution.findAnagrams(s, p))