# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first_arr = []
        second_arr = []

        while l1:
            first_arr.append(l1.val)
            l1 = l1.next

        while l2:
            second_arr.append(l2.val)
            l2 = l2.next

        num_1 = int("".join(str(num) for num in first_arr[::-1]))
        num_2 = int("".join(str(num) for num in second_arr[::-1]))

        total = str(num_1 + num_2)[::-1]

        head = ListNode(int(total[0]))
        curr = head

        for i in range(1, len(total)):
            curr.next = ListNode(int(total[i]))
            curr = curr.next

        return head
