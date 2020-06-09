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
- merge two linked lists  --> merge K sorted linked list 
- copy a list


Some tricks: 
- use a dummy node when the structure of the linked list changes
- use fast and slow pointers to record the positions of some nodes --> detect cycle
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
		
		for i in range(n - m):
			tmp = p2.next
			p2.next = p1
			p1 = p2
			p2 = tmp
		
		cut1.next = p1
		cut2.next = p2
		
		return dummy.next
		
# find the middle node

## version 1: find the left element when node number is even, [1,2,3,4] will return 2
def findMiddle(head):
	fast = head
	slow = head
	while fast and fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
	return slow
## version 2: find the right element when node number is even, [1,2,3,4] will return 3
def findMiddle(head):
	fast, slow = head, head
	while fast and fast.next:
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
		tail = taail.next
	if l1:
		tail.next = l1
	if l2:
		tail.next = l2
	
	return dummy.next
	
	
# detect cycle: fast and slow pointers, if there is a cycle, fast pointer will catch up with the slow one.
class Solution:
	
	def hasCycle(self, head):
		if not head:
			return False
		fast = head
		slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return True
		return False
		
	# method to find where cycle begins: suppose the length of the cycle is l, the distance from the start of the cycle to the head is a, the place where the fast catches up with the slow has distance b with respect to the start of the cycle, the other part of the cycle will be c = (l - b). Since the fast pointer is twice the speed of the slow one, a + l + b = 2 * (a + b) ===> a = c. Therefore, after the fast pointer meet the slow one, if we move a pointer from the head with the same speed with the fast pointer, the place where they meet will be the starting point of the cycle.
	
	def cycle_start(self, head):
		if head is None or head.next is None:
			return None
		slow = head
		fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break
				
		if slow == fast:
			slow = head
			while slow != fast:
				slow = slow.next
				fast = fast.next
			return slow
			
		return None

## copy a list with a random pointer --> hash map
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
class Solution:
	
	def copy_ramdom_list(self, head):
		my_map = {}
		nHead = RandomListNode(head.label)
		my_map[head] = nHead
		p = head
		q = nHead
		while p:
			q.random = p.random   # the copied node's random pointer still points to the original list's node 
			if p.next:
				q.next = RandomListNode(p.next.label)
				my_map[p.next] = q.next
			else:
				q.next = None
			p = p.next
			q = q.next
			
		p = nHead
		
		while p:
			if p.random:
				p.random = my_map[p.random]
			p = p.next
		
		return nHead
