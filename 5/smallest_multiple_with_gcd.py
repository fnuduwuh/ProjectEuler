# https://en.wikipedia.org/wiki/Least_common_multiple#Calculation

def get_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return get_gcd(num2, num1 % num2)

def get_lcm(num1, num2):
    return num2 * (num1 / get_gcd(num1, num2))

def get_lcm_of_range(max):
    result = max
    for i in range(1, max):
        result = get_lcm(i, result)
    return result

def run(num):
    print(int(get_lcm_of_range(num)))

run(20)