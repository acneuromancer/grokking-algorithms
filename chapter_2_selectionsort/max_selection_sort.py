def max_selection_sort(arr):

    def find_greatest(arr):
        greatest = arr[0]
        greatest_index = 0

        for i in range(0, len(arr)):
            if arr[i]  > greatest:
                greatest = arr[i]
                greatest_index = i
        
        return greatest_index

    new_arr = []

    for i in range(0, len(arr)):
        greatest = find_greatest(arr)
        new_arr.insert(0, arr.pop(greatest))
    
    return new_arr


def max_selection_sort_2(arr):
    for i in range(len(arr)-1, 0, -1):
        greatest = arr[i]
        greatest_index = i

        for j in range(0, i):
            if arr[j] > greatest:
                greatest = arr[j]
                greatest_index = j

        arr[i], arr[greatest_index] = arr[greatest_index], arr[i]