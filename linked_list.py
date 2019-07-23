class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

'''
Linked List basic methods:
- insert a node
- delete a node
- reverse from mth to nth
- find the middle 
- merge two linked lists

Some tricks: 
- use a dummy node when the structure of the linked list changes
- use pointers to record the positions of some nodes 
'''
#

# reverse from mth to nth: 2 pointers 
class Solution:
	
	def reverseBetween(self, head, m, n):
		if m > n or head is None:
		 	return head
		dummy = ListNode(0)
		dummy.next = head
		p1 = dummy
		p2 = head
		for i in range(m - 1):
			p1 = p1.next
			p2 = p2.next
		cut1 = p1
		cut2 = p2
		p1 = p1.next
		p2 = p2.next
		
		for i in range(n-m):
			tmp = p2.next
			p2.next = p1
			p1 = p2
			p2 = tmp
		
		cut1.next = p1
		cut2.next = p2
		
		return dummy.next
		
# find the middle node
def findMiddle(head):
	fast = head
	slow = head
	while fast and slow:
		fast = fast.next.next
		slow = slow.next
	return slow

# find the Nth node to the last element

def nth2Last(head, n):
	if not head:
		return head
		
	p1 = head
	p2 = head
	
	for i in range(n):
		p2 = p2.next
	while p2 and p1:
		p2 = p2.next
		p1 = p1.next
		
	return p1

# merge two sorted lists
def mergeTwoLists(l1, l2):
	dummy = ListNode(0)
	tail = dummy
	while l1 and l2:
		if l1.val < l2.val:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	if l1:
		tail.next = l1
	if l2:
		tail.next = l2
	
	return dummy.next

