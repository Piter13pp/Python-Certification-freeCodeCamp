#Video watched to understand the Quick sort algorithm: https://www.youtube.com/watch?v=Hoixgm4-P4M
def quick_sort(list):
    if not list:
        return []

    pivot = list[0]

    less = []
    equal = []
    more = []
    

    for num in list:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            equal.append(num)

    return quick_sort(less) + equal + quick_sort(more)

print(quick_sort([]))
print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))