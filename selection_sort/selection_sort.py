def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest_number = findSmallest(arr)
        new_array.append(arr.pop(smallest_number))
    return new_array

numbers = [8, 4, 10, 2, -5, 1, 5, 3, 10]

print(selection_sort(numbers))