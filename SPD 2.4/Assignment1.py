"""
Problem 1
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
"""

def two_sum(arr, t):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == t and arr[i] != arr[j]:
                return [arr[i], arr[j]]

    return []

def two_sumv2(arr, t):
    results = {}

    for val in arr:
        results[val] = True

    for val in arr:
        diff = t - val
        if diff in results:
            return val, diff

    return []

arr = [5, 3, 6, 8, 2, 4, 7]
arr2 = [1, 3, 6, 5, 8, 11]
t = 10

print(two_sumv2(arr, t))

"""
Problem 2
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]
"""

def find_k_largest(arr, k):
    arr.sort()
    n = len(arr)
    result = []

    for index in range(len(arr)):
        if index >= n - k:
            result.append(arr[index])

    return result

arr3 = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3

print(find_k_largest(arr3, k))
