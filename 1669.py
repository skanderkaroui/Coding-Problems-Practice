# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        mergeArray = []
        i = 0
        current1 = list1
        while (i < a):
            mergeArray.append(current1.val)
            current1 = current1.next
            i += 1

        current2 = list2        
        while (current2 != None):
            mergeArray.append(current2.val)
            current2= current2.next

        while(i < b +1):
            current1 = current1.next
            i += 1

        while (current1 != None):
            mergeArray.append(current1.val)
            current1 = current1.next

        result_list = None
        for x in range(len(mergeArray)):
            new_node = ListNode(mergeArray.pop(), result_list)
            result_list = new_node
        return result_list
        