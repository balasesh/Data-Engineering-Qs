# returns the number of times a given character occurs in the given string

def repeaCharCount(word, c):
    count = 0
    for i in range(len(word)):
        if(word[i].lower() == c.lower()):
            count += 1
    return count

word = 'Missisipi'
print("The count of letter \'s\' is: ",repeaCharCount(word, 's'))
print("The count of letter \'s\' is: ",repeaCharCount(word, 'i'))
print("The count of letter \'s\' is: ",repeaCharCount(word, 'm'))