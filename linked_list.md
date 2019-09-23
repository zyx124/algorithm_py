Linked List is a linear data structure. All the nodes have a pointer pointing to somewhere, the next node or none. 

Linked list is defined as:


```python         

class ListNode(object):

    def __init__(self, val, next=None):

        self.val = val
        self.next = next

```

Be careful, the structure of a linked list changes only when some node's *next* pointer changes.



Linked List basic methods:

- insert a node

- delete a node

- reverse from mth to nth

- find the middle 

- merge two linked lists  --> merge K sorted linked list 

- copy a list



## reverse from mth to nth: 2 pointers 

This is a more general solution of reversing a linked list for any portion. 

```python
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
```


## find the middle node

**version 1**: find the left element when node number is even, [1,2,3,4] will return 2
def findMiddle(head):
	fast = head
	slow = head
	while fast and fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
**version 2**: find the right element when node number is even, [1,2,3,4] will return 3
def findMiddle(head):
	fast, slow = head, head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next 
	return slow
	
## find the Nth node to the last element

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
