# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # making the words to lower case
    word = word.lower()
    anagram = anagram.lower()

    #checking the length of the words
    if(len(word) != len(anagram)):
        return False
    else: 
        if(sorted(word) != sorted(anagram)): #sorting the word for example if sorted(hey) => output 'e', 'h', 'y'
            return False
        else:
            return True #if it passes all those conditions, then it is an anagram

print(find_anagram('hello', 'lloEh')) #you can test with uppercase, lowercase,different lengths, same length, different letter and length, same letters and length 
    

