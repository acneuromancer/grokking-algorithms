def min_selection_sort(arr):
   
    def find_smallest(arr):
        smallest = arr[0]
        smallest_index = 0

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        
        return smallest_index
    
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


def min_selection_sort_2(arr):
    for i in range(0, len(arr)-1):
        smallest = arr[i]
        smallest_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
