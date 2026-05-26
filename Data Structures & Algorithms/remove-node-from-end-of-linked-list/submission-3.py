# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removenode(self,node,n):
        #处理基本情况,这个会有一个return 来传递变量
        if node is None:
            return 0
        #递的时候记录当前是第几层
        index = self.removenode(node.next,n)+1
        if index == n+1:
            node.next =node.next.next
        #这里还有一个return 来传递
        return index
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = self.removenode(head,n)
        if index ==n:
            #在 Python 中，一旦执行到 return，当前函数立即终止执行，因此当 return head.next 被触发时，后面的 return head 不会再运行。
            return head.next
        return head
        
        # # 创建一个 dummy（假头节点），指向 head
        # # 用 dummy 能统一处理“删除头节点”的情况，避免特判
        # dummy = ListNode(0, head)

        # # first 和 second 是双指针
        # # first 从 dummy 开始（指向删除节点的前一个位置）
        # # second 从 head 开始（用于领先 n 步）
        # first = dummy
        # second = head

        # # 让 second 先走 n 步，使 second 与 first 相距 n
        # while n > 0 and second:
        #     second = second.next
        #     n -= 1

        # # 让 first 和 second 一起前进
        # # 当 second 到达 None 时，first 正好停在要删除节点的前一个节点
        # while second:
        #     first = first.next
        #     second = second.next

        # # 删除链表倒数第 n 个节点：
        # # first.next 指向被删节点，跳过它即可
        # first.next = first.next.next

        # # 返回新的头节点（跳过 dummy）
        # return dummy.next


        #创建一个dummy的头节点放到前面来避免只有一个节点的时候删除掉head节点
        # dummy =ListNode(0,head)
        # #创建两个指针，一个指向dummy，后一个指向head
        # l =dummy
        # r=head
        # count = 0
        # while r is not None:
        #     r =r.next
        #     count +=1
        #     if count>n:
        #         l =l.next
        # l.next =l.next.next
        # #dummy 作为固定前驱节点，保证链表头变化时仍能通过 dummy.next 拿到正确的新头。
        # return dummy.next
        
