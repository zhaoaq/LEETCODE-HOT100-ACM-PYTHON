# 注意输出的true和false都是布尔值，所以赋值的时候赋成大写的才可以
from templates.linked_list import crateLink


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def createLink(list):
    if not list:
        return None
    for i in range(len(list) - 1):
        list[i] = list[i + 1]
    return list[0]

class Solution:

    def reverseLink(self, head):
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def getMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self,head):
        middle_node = self.getMiddleNode(head)
        reversed_link = self.reverseLink(middle_node)
        while reversed_link:
            if reversed_link.val == head.val:
                reversed_link = reversed_link.next
                head = head.next
            else:
                return False
        return True

list = input().strip().split()
head = crateLink([ListNode(int(x)) for x in list])
solution = Solution()
print(solution.isPalindrome(head))


