#返回链表开始入环的第一个节点,注意不是索引。如果链表无环，则返回 null。
class Listnode:
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def hasCircle2(self, head):
        if not head:
            return None
        else:
            slow = head
            fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None

list_str = input().strip().split()
pos = int(input())

# 连接节点
nodes = [Listnode(int(x)) for x in list_str]
for i in range(len(list_str) - 1):
    nodes[i].next = nodes[i + 1]

# 处理成环
if -1 < pos < len(list_str) - 1:
    nodes[len(list_str) - 1].next = nodes[pos]

solution = Solution()
print(solution.hasCircle2(nodes[0]))