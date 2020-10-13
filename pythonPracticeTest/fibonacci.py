# def fibonacci(n):
#     if n < 0:
#         print ("Incorrect Input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(100))

# FibArray = [0,1] 
  
# def fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     elif n<=len(FibArray): 
#         return FibArray[n-1] 
#     else: 
#         temp_fib = fibonacci(n-1)+fibonacci(n-2) 
#         FibArray.append(temp_fib) 
#         return temp_fib 
  
# print(fibonacci(5)) 

def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
    return b 
  
# Driver Program 
  
print(fibonacci(2000)) 