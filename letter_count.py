word = input("Enter a word ")
letter = input("Enter a letter in the word ")

count = word.count(letter)
if count > 0:
    print("{} occurs {} times in {}".format(letter, count, word))
else:
    print("Letter is not in word")