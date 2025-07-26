# 套圈算法和相交链表一样，快慢指针和getMiddleNode类似
from problems.Hashing.p049_Group_Anagrams.main import solution


class LinkNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def hasCircle(self,head):
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

list = input().strip().split()
pos = int(input())
nodes = [LinkNode(int(x)) for x in list]
# 构造环形链表
if pos != -1 and pos < len(nodes):
    nodes[-1].next = nodes[pos]
if nodes


solution = Solution()
print(solution.hasCircle(head))



