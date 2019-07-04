"""
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""


def solution(ll):
    if ll.size % 2 == 0:
        middle_index = ll.size / 2
        curr_node = ll.head
        for _ in range(1, middle_index):
            curr_node = curr_node.next
        return curr_node.data
    else:
        middle_index = ll.size // 2
        curr_node = ll.head
        for _ in range(1, middle_index):
            curr_node = curr_node.next
        return curr_node.data, curr_node.next.data
