# 注意节点的定义类和别的有所不同
class Listnode:
    def __init__(self, data, next = None):
        self.val = data
        self.next = next

class Solution:
    def addTwoNums(self, l1, l2, carry):
        if l1 is None and l2 is None and carry == 0:
            return
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        return Listnode(carry % 10, self.addTwoNums(l1, l2, carry // 10))

def createLink(list_str):
    if not list_str:
        return None
    for i in range(len(list_str) - 1):
        list_str[i].next = list_str[i + 1]

    return list_str[0]

def printLink(head):
    while head:
        print(head.val, end=" ")
        head = head.next

l1_str = input().strip().split()
l2_str = input().strip().split()
l1 = createLink([Listnode(int(x)) for x in l1_str])
l2 = createLink([Listnode(int(x)) for x in l2_str])

solution = Solution()
printLink(solution.addTwoNums(l1, l2, 0))
