def sum(arr):
    total = 0
    
    for i in arr:
        total += i

    return total


def sum_recursive(arr):
    if arr == []:
        return 0

    return arr[0] + sum_recursive(arr[1:])


print(sum([2, 4, 5, 6]))
print(sum_recursive([2, 4, 5, 6]))