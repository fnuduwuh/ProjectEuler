# input is maximale nummer (dus voor 3-digit numbers zoals opgave is de max 999)
# palindrome checker loopt de hoogste honder nummers af en retourneert het eerste palindroom
# als deze hoger is dan de huidige max_palindrome wordt deze overschreven

def run_palindrome_checker(max_number):
    max_palindrome = 0
    number_to_check = max_number
    while max_number - number_to_check < 100: # check alleen de hoogste 100 t.b.v. performance
        uitkomst: int = palindrome(number_to_check)
        if uitkomst > max_palindrome:
            max_palindrome = uitkomst
        number_to_check -= 1
    print(max_palindrome)

def palindrome(number_to_check):
    num = number_to_check
    for i in range(num):
        if is_palindrome(num * number_to_check):
            return num*number_to_check
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

run_palindrome_checker(999)