def palindrome(max_number):
    num = max_number
    for i in range(num):
        if is_palindrome(num*max_number):
            print(str(num) + ' keer ' + str(max_number) + ' is ' + str(num * max_number))
            return num*max_number
        else:
            num -= 1
    return 0

def is_palindrome(number):
    length = len(str(number))
    for i in range(length):
        num1 = str(number)[i]
        num2 = str(number)[length - (i+1)]
        if num1 != num2:
            return False
    return True

def run_palindrome_checker(number):
    max_palindrome = 0
    number_to_check = number
    while number - number_to_check < 100: # check alleen de hoogste 100 t.b.v. performance
        uitkomst: int = palindrome(number_to_check)
        if uitkomst > max_palindrome:
            max_palindrome = uitkomst
        number_to_check -= 1
    print(max_palindrome)

run_palindrome_checker(999)