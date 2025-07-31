class Listnode:
    def __init__(self, data):
        self.val = data
        self.next = None

def createLink(node_list):
    if not node_list:
        return None
    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i + 1]
    return node_list[0]

def printLink(head):
    while head:
        print(head.val, end=" ")
        head = head.next

class Solution:
    def merge(self, head1, head2):
        dummy = Listnode(-1)
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            # 易错点：别忘了cur也要更新
            cur = cur.next
        cur.next = head1 or head2
        return dummy.next

list_str1 = input().strip().split()
list_str2 = input().strip().split()
list_str1 = [Listnode(int(x)) for x in list_str1]
list_str2 = [Listnode(int(x)) for x in list_str2]
head1 = createLink(list_str1)
head2 = createLink(list_str2)
solution = Solution()
printLink(solution.merge(head1, head2))