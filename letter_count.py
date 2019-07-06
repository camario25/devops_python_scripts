word = input("Enter a word ")
letter = input("Enter a letter in the word ")

letter_count = word.count(letter)
if letter_count == 1:
    print("{} occurs {} time in {}".format(letter, letter_count, word))
elif letter_count > 1:
    print("{} occurs {} times in {}".format(letter, letter_count, word))
else:
    print("Letter is not in word")