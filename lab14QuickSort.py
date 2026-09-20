def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    pivot = arr[0] 
    less = [x for x in arr if x < pivot]
    equal = [y for y in arr if y == pivot]
    greater = [e for e in arr if e > pivot]
    quick_sort(less)
    quick_sort(greater)
    return quick_sort(less) + equal + quick_sort(greater)
