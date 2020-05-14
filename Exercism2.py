def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError('search list is empty')

    left_pointer = 0
    right_pointer = len(search_list) - 1

    while left_pointer <= right_pointer:
        mid_index = (left_pointer + right_pointer) // 2
        mid_value = search_list[mid_index]

        if mid_value == value:
            return mid_index
        elif mid_value < value:
            left_pointer = mid_index + 1
        else:
            right_pointer = mid_index - 1

    raise ValueError('Value not in search list')
