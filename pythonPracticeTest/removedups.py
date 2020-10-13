
from collections import Counter 
  
# def find_dup_char(input): 
  
#     # now create dictionary using counter method 
#     # which will have strings as key and their  
#     # frequencies as value 
#     WC = Counter(input) 
#     j = -1
      
#     print(WC)  
#     # Finding no. of  occurrence of a character 
#     # and get the index of it. 
#     for i in WC.values(): 
#         j = j + 1   
#         if( i > 1 ): 
#             vocab = list(WC.keys())
#             print(vocab[j])

def find_dup_char(input): 
    d = {}
    for i in range(len(input)):
        if not input[i] in d.keys():
            d[input[i]] = 1
        else:
            d[input[i]] += 1

    for x in d.items():
        if x[1] > 1:
            print(x[0])
    return d

def sortDict(d):
    return sorted( d.items(), key = lambda x : x[1], reverse = False)
    

# Driver program 
if __name__ == "__main__": 
    input = 'geeksforgeeks'
    d = find_dup_char(input) 
    print(sortDict(d))
