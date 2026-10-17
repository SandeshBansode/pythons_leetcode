class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        size = 1

        while size < length:
            tail = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                merged_head, merged_tail = self.merge(left, right)

                tail.next = merged_head
                tail = merged_tail

            size *= 2

        return dummy.next

    def split(self, head, size):
        if not head:
            return None

        for _ in range(size - 1):
            if not head.next:
                break
            head = head.next

        second = head.next
        head.next = None

        return second

    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        tail.next = left if left else right

        while tail.next:
            tail = tail.next

        return dummy.next, tail