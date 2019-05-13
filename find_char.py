def main():
    def find_char():
        user_char = input("Enter one character you would like to find in a string ").strip()
        if user_char == '':
            print('no white space characters please')
            find_char()
        user_string = input("Enter a string ").strip()
        if user_string:
            char_count = user_string.count(user_char)
            print("'{}' occurs {} times in the string".format(user_char, char_count))
    find_char()

main()