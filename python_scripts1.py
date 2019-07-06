
string_word = input("Enter a word: ")
upper_str = string_word.upper()
if string_word == upper_str:
    print("Your input " + string_word + " is already all uppercase")
else:
    print(string_word + " is now uppercase " + upper_str)