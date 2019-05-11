def upper_case(string_input):
    for i in string_input:
        return str(chr(ord(i)-32))


print(ord('a'))
print(ord('A'))
print(upper_case('adbc'))