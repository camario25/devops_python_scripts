def reverse_words():
    user_words = input("Enter three words to reverse ")
    user_arr = user_words.split()
    rev_words = ' '.join(user_arr[::-1])
    print("New order is {}".format(rev_words))

def main():
    while True:
        reverse_words()
        quest = input("Would you like to try more words? write 'yes' or 'no': ")
        if quest == 'no' or quest == 'n':
            break

main()