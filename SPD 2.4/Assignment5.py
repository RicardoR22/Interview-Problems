"""
Given a singly-linked list, find the middle value in the list.
Example: If the given linked list is A → B → C → D → E, return C.
Assumptions: The length (n) is odd so the linked list has a definite middle.
"""
import math
import LinkedList
ll = LinkedList.LinkedList
node = LinkedList.Node

def find_middle_node(ll):
    length = ll.size
    if length % 2 == 0:
        middle_node = length / 2
    else:
        middle_node = math.ceil(length / 2)

    curr_node = ll.head

    count = 1
    while count < middle_node:
        curr_node = curr_node.next
        count += 1

    if length % 2 == 0:
        return curr_node, curr_node.next
    else:
        return curr_node



ll1 = ll()
for i in range(1, 6):
    ll1.append(node(i))
print(ll1)
print(find_middle_node(ll1))

ll2 = ll()
for i in range(1, 7):
    ll2.append(node(i))
print(ll2)
print(find_middle_node(ll2))




"""
Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.
Example: If the given linked list is A → B → C → D → E,
nodes should be modified/rearranged so the list becomes E → D → C → B → A.
"""


def reverse_ll(ll):
    prev_node = None
    curr_node = ll.head
    next_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    ll.head = prev_node

    return ll


print(reverse_ll(ll1))
