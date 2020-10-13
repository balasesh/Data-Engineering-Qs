def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
    print(i,": ",str)
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ") 
print (s) 
  
print ("The reversed string(using loops) is : ") 
print (reverse(s)) 