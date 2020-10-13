# Add to dictionaty 
d = {0: 10, 1: 20}
d[2] = 30
# d.update({'a': 1})
# # OR
# d.update(dict(a=1))
# # OR
# d.update(a=1)

print(d)

# concatenate 2 or more dictionaries

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

def hasKey(key): 
    if dic1.get(key) : 
        return True
    else : 
        return False

print(hasKey(10))
print(hasKey(1))