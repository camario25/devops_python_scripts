while True:
    try:
        user_input = float(input('enter a number '))
        if user_input > 0:
            print('number is positive')
        elif user_input < 0:
            print('number is negative')
        else:
            print('number is zero')
        break
    except ValueError:
        print('input must be a real number')
