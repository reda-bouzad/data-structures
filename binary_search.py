# Declarting An array
# people = ["ahmed", "Badr", "Chadi", "Reda"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for number in numbers:
#     print(number)

def binary_search(list, item):
# Declaring Low, high, mid and guess
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None;
    
print(binary_search(numbers, 8))





