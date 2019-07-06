

def main():
    while True:
        user_suffix = input("Enter a suffix to remove from words ")
        user_word = input("Enter a word with suffix ")
        remove_suffix(user_suffix,user_word)
        quest = input("Would you like try another word? write 'yes' or 'no': ")
        if quest == 'no' or quest == 'n':
            break

        
def remove_suffix(user_suffix, user_word):
    if user_word.endswith(user_suffix):
        new_word = user_word[:-len(user_suffix)]
        print("New word is {}".format(new_word))
    else:
        print("Word does not contain '{}' suffix".format(user_suffix))

main()


