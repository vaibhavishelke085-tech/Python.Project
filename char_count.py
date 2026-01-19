user_input = input("Enter a word or sentence: ")
char_count = {}
for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1   
print("Character count:", char_count)