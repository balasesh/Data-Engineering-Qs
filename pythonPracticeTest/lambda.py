# [('b', 12), ('a', 4), ('c', 3)]
d = {"a": 4, "c": 3, "b": 12}
[(k, v) for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)]
# sort a dict based on value