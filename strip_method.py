def main():
    user_suffix = input("Enter a suffix to remove from words ")
    def remove_suffix():
        user_word = input("Enter a word with suffix ")
        if user_word.endswith(user_suffix):
            new_word = user_word[:-len(user_suffix)]
            print("New word is {}".format(new_word))
    remove_suffix()
    quest = input("Would you like add another word? write 'yes' or 'no'")
    if quest == 'no' or quest == 'n':
        exit()
    else:
        remove_suffix()

main()