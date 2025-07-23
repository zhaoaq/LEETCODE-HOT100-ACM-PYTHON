# 构建节点
class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

# 构建链表
def crateLink(list):
    if not list:
        return None
    for i in range(len(list) - 1):
        list[i].next = list[i + 1]
    return list[0]

# 打印链表
def printLink(head):
    if head:
        print(head.val, end = " ")
        head = head.next

# 获取中间节点（偶数个则是中间偏右）
def getMiddleNode(head):
    slow = head
    fast = head
    # 同时满足这两个条件，fast指针才可以移动两步
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
