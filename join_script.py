def main():
    user_suffix = input("Enter a suffix to add to words ")
    def add_suffix():
        user_word = input("Enter a word to add suffix ")
        new_word = ''.join([user_word, user_suffix])
        print("New word is {}".format(new_word))
    add_suffix()
    quest = input("Would you like try another word? write 'yes' or 'no'")
    if quest == 'no' or quest == 'n':
        exit()
    else:
        add_suffix()

main()