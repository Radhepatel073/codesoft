import random
import string

letter = string.ascii_letters

digits =string.digits

uppercase_digit =string.ascii_lowercase

lowercase_digit =string.ascii_uppercase

special_char = string.punctuation

main_count = int(input("enter the number for the length password"))
print(f'you have selected{main_count} number of password')



main_string = []
main_string.extend(letter)
main_string.extend(digits)
main_string.extend(uppercase_digit)
main_string.extend(lowercase_digit)
main_string.extend(special_char)

random.shuffle(main_string)
print(''.join(main_string[0:main_count]))



