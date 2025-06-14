# 滑动窗口（双指针实现）

class Solution:
    def lengthOfLongestSubstring(self,s:str):
        window = set()
        n = len(s)
        left = 0
        right = 0
        res = 0
        while right < n:
            # 右侧不在窗口里面,加入窗口
            if s[right] not in window:
                window.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                #易错点：不要忘记移除左边的
                window.remove(s[left])
                left += 1

        return res

s = input()
#print(s)

solution = Solution()
print(solution.lengthOfLongestSubstring(s))
