
string_word = input("Enter a word: ")
upper_str = string_word.upper()
if string_word == upper_str:
    print("No lowercase letters in: " + string_word)
else:
    print(string_word + " is now uppercase " + upper_str)