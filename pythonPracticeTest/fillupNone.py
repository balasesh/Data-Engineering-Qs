# Given an array containing None values fill in the None values with most recent non None value in the array
# - input array: [1,None,2,3,None,None,5,None]
#  - output array: [1,1,2,3,3,3,5,5]

def mostRecentNonNull(arr):
    if not arr: 
        return arr
    temp = None
    for i in range(len(arr)):
        if arr[i] == None:
            arr[i] = temp
        else : 
            temp = arr[i] 
    return arr

arr = [1,None,2,3,None,None,5,None]
print("Test 1 - Before Change: ", str(arr))
print(mostRecentNonNull(arr))

arr1 = [None,None,1,2,3,None,None,5,None]
print("Test 2 - Before Change: ", str(arr1))
print(mostRecentNonNull(arr1))

arr2 = []
print("Test 2 - Before Change: ", str(arr2))
print(mostRecentNonNull(arr2))

arr3 = [None,None]
print("Test 2 - Before Change: ", str(arr3))
print(mostRecentNonNull(arr3))