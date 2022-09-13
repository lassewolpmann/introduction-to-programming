# INDEXES
lst = [2, 5, 8]                 # Creating list with name "lst" with items 2, 5 and 8
print(lst[1])                   # Accessing second index of list

lst[1] = 10                     # Changing second index from 5 -> 10
print(lst)                      # Printing out the whole list

s = 'abcdefg'                   # Setting variable "s" as 'abcdefg'
print(s[0])                     # Print first index of s
print(s[1])                     # Print second index of s
print(len(s))                   # Getting the length of s
# print(s[7])                   # This wouldn't work, because indexes start at 0 and 7 is an invalid index
print(s[6])                     # Manual way of getting last index
print(s[len(s) - 1])              # Long automatic way of getting last index
print(s[-1])                    # Correct way of getting last index

# SLICES
word = 'ammattikorkeakoulu'     # Setting variable "word"
print(word[0:7])                # Printing out the indexes 0 to 6 (7 is excluded) -> ammatti
print(word[7:13])               # Printing out the indexes 7 to 12 (13 is excluded) -> korkea
print(word[13:])                # Printing out from index 13 to last -> koulu
print(word[:])                  # Printing out from first to last index -> whole string gets printed
print(word[:7])                 # Same as word[0:7], printing out first to 7th index
print(word[::2])                # Skipping every odd index
print('redrum'[::-1])           # Printing out in reverse

w = 'saippuakauppias'
print(w == w[::-1])             # Test if the two variables are equal (True or False)

print(lst[::-1])               # Printing out a list in reverse
