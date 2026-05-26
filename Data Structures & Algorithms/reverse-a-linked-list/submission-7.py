# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
   # 使用递归反转链表的辅助函数
    def recursives(self, curr, pre):
        # 基本情况：当前节点为空，说明链表已全部反转完成，pre 即为新头节点
        if not curr:
            return pre

        # 当前层的处理：保存下一个节点，并反转当前节点的指针
        nex = curr.next
        curr.next = pre

        # 递归处理剩余链表，将当前节点作为下一层的 pre
        newhead = self.recursives(nex, curr)

        # 回溯阶段逐层返回最终的新头节点
        return newhead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursives(head,None)

    #     # pre 指向“已反转部分”的表头；一开始还没有反转任何节点，所以是 None
    #     pre = None
    #     # curr 是工作指针，从当前还未反转的链表头开始走
    #     curr = head

    #     # ⚠️ 易错点：一定是 while curr（谁在变就看谁），不要写 while head
    #     while curr:
    #         # 1) 先保存下一节点。⚠️ 不提前保存会在下一步断链后丢失后半段
    #         nxt = curr.next

    #         # 2) 核心反转：把当前节点的 next 指向“前一个”（也就是已反转部分的表头 pre）
    #         curr.next = pre

    #         # 3) 两个指针整体右移：pre 前进一步成为新的表头；curr 继续处理下一节点
    #         pre = curr
    #         curr = nxt

    #     # 循环结束时：
    #     # - curr == None（已经走到尾部之后）
    #     # - pre 指向“反转后链表”的新表头
    #     # ⚠️ 易错点：必须 return pre，而不是 return head（head 仍指向旧的第一个节点，此时已变成尾巴）
    #     return pre

        
    # class Solution:
    #     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #         # 1) 递归终止条件：
    #         #    如果链表为空，直接返回 None（没有东西可以反转）
    #         if not head:
    #             return None
            
    #         # 默认把当前节点当作“最终的新表头”（兜底返回值）
    #         # 如果后面没有节点，这个值会直接被返回
    #         newhead = head

    #         # 2) 如果当前节点后面还有节点，
    #         #    就先把“后半段链表”全部反转好（后序递归）
    #         if head.next:
    #             # 2.1 递归处理下一段链表，并拿到“反转后的新表头”
    #             newhead = self.reverseList(head.next)

    #             # 2.2 此时 head.next 指向的是“反转后链表的最后一个节点”
    #             #     把它的 next 指向当前节点，实现指针翻转
    #             head.next.next = head

    #             # 2.3 将当前节点的 next 断开（避免形成环）
    #             head.next = None

    #         # 3) 把整个链表反转后的新表头（来自最底层）返回给上层
    #         return newhead
