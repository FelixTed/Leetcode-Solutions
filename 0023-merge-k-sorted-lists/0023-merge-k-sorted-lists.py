# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        curr = ListNode(0,None)
        beforeHead = curr

        thereIsANode = True
        while thereIsANode:
            thereIsANode = False
            minNode = ListNode(1001,None)
            minIndex = 0
            for i in range(len(lists)):
                if lists[i]:
                    thereIsANode = True
                    if minNode.val > lists[i].val:
                        minNode = lists[i]
                        minIndex = i
            if not thereIsANode:
                break
            lists[minIndex] = lists[minIndex].next
            curr.next = minNode
            curr = curr.next
        return beforeHead.next
        