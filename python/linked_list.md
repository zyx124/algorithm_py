Linked List is a linear data structure. All the nodes have a pointer pointing to somewhere, the next node or none. 

Linked list is defined as:


```python

class ListNode(object):

    def __init__(self, val, next=None):

        self.val = val
        self.next = next

```

One thing to be noticed is that the structure of a linked list changes only when some node's *next* pointer changes.


Linked List basic methods:

- insert a node
- delete a node
- reverse from mth to nth
- find the middle 
- merge two linked lists  --> merge K sorted linked list 
- copy a list


## Reverse a Linked List 

```python
class Solution:
	
	def reverse(self, head):
		cur = None
		
		while head:
			temp = head.next
			head.next = cur
			cur = head
			head = temp
		
		return cur
```


## Reverse From mth to nth (2 pointers)

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


## Find the Middle Node

**version 1**: find the left element when node number is even, [1,2,3,4] will return 2

```python
def findMiddle(head):
	fast = head
	slow = head
	while fast and fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
```

**version 2**: find the right element when node number is even, [1,2,3,4] will return 3

```python
def findMiddle(head):
	fast, slow = head, head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next 
	return slow
```

## Find the Nth Node to The Last Element

```python
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
```

## How to detect a cycle

If there is a cycle, the linked list will have a infinite loop when we use a pointer to traverse the list. Therefore, we can use two pointers, one fast and the other slow, to traverse the linked list. If there is a cycle, the fast pointer will wait the slow pointer. If they meet somewhere, we can stop and declare that we have found the cycle.

```python
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
```

Further, we may also want to know where the cycle starts. Some calculation is needed here. Suppose the length of the cycle is *l*, the distance from the start of the cycle to the head is *a*, the place where the fast catches up with the slow has distance *b* with respect to the start of the cycle, the other part of the cycle will be *c = (l - b)*. Since the fast pointer is twice the speed of the slow one, *a + l + b = 2(a + b)* ===> *a = c*. Therefore, after the fast pointer meet the slow one, if we move a pointer from the head with the same speed with the fast pointer, the place where they meet will be the starting point of the cycle.

```python
class Solution:
	
	def cycle_start(self, head):
		if not head or not head.next:
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
```

## Copy a Linked List With a Random Pointer
```python
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
```





