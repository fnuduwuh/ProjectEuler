def smallest_multiple(max_num):
    result = max_num
    cont = True
    while cont:
        cont = not is_divisible_by_all(result, max_num)
        result += 1

def is_divisible_by_all(num_to_check, max_num):
    for i in range(2, max_num):
        if num_to_check % i != 0:
            return False
    print(num_to_check)
    return True

smallest_multiple(20)