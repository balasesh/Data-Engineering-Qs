# Write a Python script to sort (ascending and descending) a dictionary by value

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d_asc = sorted(d.items(), key = lambda x : x[1], reverse=False)
d_dsc = sorted(d.items(), key = lambda x : x[1], reverse=True)

print(d_asc)
print(d_dsc)