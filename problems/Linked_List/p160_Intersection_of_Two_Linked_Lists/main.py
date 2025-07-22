# 两个链表如果仅仅值相同，但是内存地址不同，那么它们就无法相等。
# 真正的相交是指 listA 和 listB 的某个节点是同一个对象（nodeA.next is nodeB.next）
# 用 intersectVal 和 skipA、skipB 描述相交位置，让我们手动构造相交链表。
from typing import List

class Solution:
    def getIntersectionNode(self, headA, headB):
        p, q = headA, headB
        while headA is not headB:
            headA = headA.next if headA else q
            headB = headB.next if headB else p

        return headA

# 创建节点
class Listnode:
    def __init__(self, data):
        self.val = data # data
        self.next = None # pointer

# 接收一个列表，创建为一个链表
def createList(nums: List):
    # 如果列表为空，则返回None空链表
    if not nums:
        return None
    # 类型转换：列表不为空，处理成int类型列表
    nodes = [Listnode(i) for i in nums]
    # 按照链表定义连接列表中的节点为链表
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]

def main():
    intersectVal = int(input())
    listA_str = input().strip().split()
    listB_str = input().strip().split()
    skipA = int(input())
    skipB = int(input())
    # print(intersectVal, listA, listB, skipA, skipB)

    listA = createList([int(x) for x in listA_str])
    listB = createList([int(x) for x in listB_str])

    # 如果intersectVal = 0，就不必构造内存结构指向一致
    # intersectVal > 0，构造指向一致
    if intersectVal > 0:
        # 找到相交节点前的一个标志,注意skip - 1
        nodeA = listA
        for _ in range(skipA - 1):
            nodeA = nodeA.next

        nodeB = listB
        for _ in range(skipB - 1):
            nodeB = nodeB.next

        if nodeB and nodeA:
            nodeB.next =nodeA.next


    solution = Solution()
    result_node = solution.getIntersectionNode(listA, listB)
    if result_node:
        print(f"Intersected at {result_node.val}")
    else:
        print("No intersection")

if __name__ == "__main__":
    main()














