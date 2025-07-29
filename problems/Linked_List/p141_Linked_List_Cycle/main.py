# 套圈算法和相交链表一样，快慢指针和getMiddleNode类似

class LinkNode:
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def hasCircle(self,head):
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def main():
    list_str = input().strip().split()
    pos = int(input())

    nodes = [LinkNode(int(x)) for x in list_str]

    # 连接节点
    for i in range(len(nodes) - 1):
        if nodes[i]:
            nodes[i].next = nodes[i + 1]
    # 构造环形链表
    if pos != -1 and pos < len(nodes):
        nodes[len(nodes) - 1].next = nodes[pos]

    solution = Solution()
    print(solution.hasCircle(nodes[0]))

if __name__ == "__main__":
    main()



