"""
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.
Write your answers to these questions and code answer in a repo:

What clarifying questions would you ask?
Should I return the same linked list, or a new one?

What reasonable assumptions could you state?
Is it safe to assume the linked list will not be empty?

What are 2-3 ways you can simplify the problem?


Brainstorm 2-3 ways to approach the problem.
traverse the linked list

Choose one idea and write pseudocode for it.
"""
import LinkedList
ll = LinkedList.LinkedList
node = LinkedList.Node

def rotate(ll, k):
    if k == 0:
        return

    curr_node = ll.head
    tail = ll.tail

    count = 1
    while count <= k:
        next_node = curr_node.next
        ll.head = ll.head.next
        curr_node.next = None
        tail.next = curr_node
        tail = tail.next
        ll.tail = ll.tail.next
        curr_node = next_node
        count += 1

    return ll

ll1 = ll()
for i in range(1, 10):
    ll1.append(node(i))

print(ll1)

ll1_rotated = rotate(ll1, 4)
print(ll1_rotated)
