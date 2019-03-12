def max_rec(arr):
    if len(arr) == 1:
        return arr[0]

    rec_result = max_rec(arr[1:])

    return arr[0] if arr[0] > rec_result else rec_result


def min_rec(arr):
    if len(arr) == 1:
        return arr[0]

    rec_result = min_rec(arr[1:])

    return arr[0] if arr[0] < rec_result else rec_result


arr = [301, -10, 300, -1000, 50, 45]
print("Array: ", arr)
print("Max: ", max_rec(arr))
print("Min: ", min_rec(arr))