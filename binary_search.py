def binary_search(alist, target, sort = True):
    if len(alist) == 1:
        if alist[0] == target:
            return True
        else:
            return False
    
    sort_list = alist

    if sort:
        sort_list.sort()
    
    first = 0
    last = len(alist) - 1
    middle = (first + last) // 2
    
    if sort_list[middle] == target:
        return True
    elif sort_list[middle] > target:
        return binary_search(sort_list[:middle], target, False)
    else:
        return binary_search(sort_list[middle + 1:], target, False)

list_example = [12, 8, 22, 14, 19, 27, 5, 31, 30]

print(binary_search(list_example, 30))
