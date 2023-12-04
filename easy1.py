def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

#taking input 
input_string = ('enter the sting ')
result = length_of_last_word(input_string)
print(result)
