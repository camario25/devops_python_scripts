def main():
    def your_name():
        user_name = input("Enter your name ")
        strp_name = user_name.strip()
        name_arr = strp_name.split()
        if len(name_arr) == 0:
            your_name()
        elif len(name_arr) == 1:
            print("Your First name is: {}".format(name_arr[0]))
        elif len(name_arr) == 2:
            print("Your First name is: {} and Last name is: {}".format(name_arr[0],name_arr[1]))
        elif len(name_arr) == 3:
            print("Your First name is: {}, Middle name is: {}, and Last name is: {}".format(name_arr[0],name_arr[1],name_arr[2]))
        else:
            print("You have way too many names!")
    your_name()
    quest = input("Would you like to try another name? write 'yes' or 'no'")
    if quest == 'no' or quest == 'n':
        exit()
    else:
        your_name()

main()