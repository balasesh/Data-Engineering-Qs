def my_function():
    age = 36
    state = 'alive'
    txt = "My name is John, and I am {} and i want to be {}"
    print(txt.format(age, state))
    fruits = ["apple", "banana", "cherry"]
    fruits.append("Orange")
    print(fruits)

my_function()

def my_func():
    fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    count = 0
    for x in fruits:
        count += 1
    
    print(count)

my_func()