def binary_search(whereToFind , whatToFind , low, high):
    if high<low:
        return -1
    mid = (low + high) // 2
    if whatToFind < whereToFind[mid]:
        return binary_search(whereToFind, whatToFind, low, mid-1 )
    elif whatToFind > whereToFind[mid]:
        return binary_search(whereToFind, whatToFind, mid +1, high)
    else:
        return mid


arr = [2, 4, 8, 10, 13, 17, 25, 28, 30, 40]
element = 13
loc = binary_search(arr, element, 0, len(arr)-1)
if loc == -1:
    print("Element ", element, " not found")
else:
    print("Element ", element, " found in position ", loc)