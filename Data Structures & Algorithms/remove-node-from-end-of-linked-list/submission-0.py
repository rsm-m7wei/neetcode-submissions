# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个 dummy（假头节点），指向 head
        # 用 dummy 能统一处理“删除头节点”的情况，避免特判
        dummy = ListNode(0, head)

        # first 和 second 是双指针
        # first 从 dummy 开始（指向删除节点的前一个位置）
        # second 从 head 开始（用于领先 n 步）
        first = dummy
        second = head

        # 让 second 先走 n 步，使 second 与 first 相距 n
        while n > 0 and second:
            second = second.next
            n -= 1

        # 让 first 和 second 一起前进
        # 当 second 到达 None 时，first 正好停在要删除节点的前一个节点
        while second:
            first = first.next
            second = second.next

        # 删除链表倒数第 n 个节点：
        # first.next 指向被删节点，跳过它即可
        first.next = first.next.next

        # 返回新的头节点（跳过 dummy）
        return dummy.next
