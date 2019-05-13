def main():
    def double_input():
        while True:
            try:
                user_input = float(input('Enter a number to double '))
                double = user_input * 2
                print(double)
                return double
            except ValueError:
                print('Input must be a number')
    double_input()
    quest = input("Would you like try another number? write 'yes' or 'no'")
    if quest == 'no' or quest == 'n':
        exit()
    else:
        double_input()

main()