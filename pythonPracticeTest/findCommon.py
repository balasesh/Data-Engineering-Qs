# Given two sentences, construct an array that has the words that appear in one sentence and not the other.

def findCommon(s1, s2):
    if not s1 or not s2:
        return []
    arr1 = s1.split()
    arr2 = s2.split()
    return list(set(arr1).symmetric_difference(set(arr2)))

    # newArr = []
    # for i in range(len(arr1)) :
    #     if not arr1[i] in arr2:
    #         newArr.append(arr1[i])

    # for i in range(len(arr2)) :
    #     if not arr2[i] in arr1:
    #         newArr.append(arr2[i])
    # return newArr



def findUnCommon(s1, s2):
    if not s1 or not s2:
        return []
    arr1 = s1.split()
    arr2 = s2.split()
    return list(set(arr1).intersection(set(arr2)))

    # newArr = []
    # for i in range(len(arr1)) :
    #     if arr1[i] in arr2 and arr1[i] not in newArr :
    #         newArr.append(arr1[i])

    # for i in range(len(arr2)) :
    #     if arr2[i] in arr1 and arr2[i] not in newArr :
    #         newArr.append(arr2[i])
    # return newArr


s1 = "\nThis is a dummy string"
s2 = "All is well string"
print(s1)
print(s2)
print("The common array is: ", findCommon(s1, s2))
print("The common array is: ", findUnCommon(s1, s2))


s1 = "\nThis is a dummy string"
s2 = "This is not a dummy string"
print(s1)
print(s2)
print("The new array is: ", findCommon(s1, s2))
print("The uncommon array is: ", findUnCommon(s1, s2))