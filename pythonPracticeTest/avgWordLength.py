# Calculate the average word length.

def avgWordLen(a):
    count = 0
    arr = []
    if not a:
        return "Empty"
    if isinstance(a, list):
        arr = a
    else:
        arr = a.split()
    for i in range(len(arr)):
        count += len(arr[i])
    return count/ len(arr)


print("This is an Array")
a = ["This","is","a","avg","word","sentence"]
print("Average word Length = ", avgWordLen(a))


print("\nThis is a Sentence")
b = "This is a avg word sentence"
print("Average word Length = ", avgWordLen(b))

print("\nThis is an empty array")
c = []
print("Average word Length = ", avgWordLen(c))

print("\nThis is a empty sentence")
d = ""
print("Average word Length = ", avgWordLen(d))
