""" 2. Add Two Numbers

> You are given two non-empty linked lists representing two
 non-negative integers. The digits are stored in reverse order
 and each of their nodes contain a single digit. Add the two
 numbers and return it as a linked list.

> You may assume the two numbers do not contain any leading zero,
 except the number 0 itself.

- Example Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""


class Node(object):
    """ Definition for singly-linked list.
    """
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next

    def __repr__(self):
        ret = [self.val]
        _next = self.next
        while _next:
            ret.append(_next.val)
            _next = _next.next
        return ' -> '.join(map(str, ret))


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode a
        """
        head, node = None, None
        cur1, cur2, tmp = l1, l2, 0
        while cur1 or cur2 or tmp:
            if cur1:
                cur1, val1 = cur1.next, cur1.val
            else:
                val1 = 0
            if cur2:
                cur2, val2 = cur2.next, cur2.val
            else:
                val2 = 0
            tmp, _sum = 0, val1 + val2 + tmp
            if _sum >= 10:
                tmp, _sum = 1, _sum % 10
            if node is None:
                node = Node(_sum)
                head = node
            else:
                node.next = Node(_sum)
                node = node.next
        return head


if __name__ == '__main__':
    l1 = Node(2, Node(4, Node(3)))
    l2 = Node(5, Node(6, Node(4)))
    print(l1, l2)
    print(Solution().addTwoNumbers(l1, l2))

