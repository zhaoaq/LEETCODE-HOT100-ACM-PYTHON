# 节点构造
class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

#构造链表：别忘了对空链表的处理
def createLink(list):
    if not list:
        return None
    for i in range(len(list) - 1):
        list[i].next = list[i + 1]
    return list[0]

class Solution:
    def reverseList(self, head: [ListNode]):
        cur = head #1-2-3-x
        pre = None #x
        # 每个等式右边都是下一个等式的左边
        while cur:
            nxt = cur.next # 2-3-x  3-x
            cur.next = pre # x-1    x-1-2
            pre = cur # pre = x-1   x-1-2
            cur = nxt # cur = 2-3-x    3-x
        return pre

list = input().strip().split()
# print(list)
link = createLink([ListNode(int(x)) for x in list])
solution = Solution()
result_link = solution.reverseList(link)
# print(link) 直接会输出地址
while result_link:
    print(result_link.val, end = " ") #end使输出元素不换行
    result_link = result_link.next
