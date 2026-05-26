# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 🧠 初始化快慢指针，都从链表头节点出发
        slow = head          # 每次走一步
        fast = head          # 每次走两步

        # 🧩 只要 fast 和 fast.next 不为空，就还能继续走
        # fast 是跑两步的指针，它最容易越界，所以只检查 fast 即可
        while fast and fast.next:
            slow = slow.next             # slow 走一步
            fast = fast.next.next        # fast 走两步

            # 🎯 如果 slow 和 fast 在某个时刻相遇
            # 说明 fast 在环里追上了 slow → 链表有环
            if slow == fast:
                return True

        # 🚫 fast 越界了（到达 None）→ 不可能有环
        return False
