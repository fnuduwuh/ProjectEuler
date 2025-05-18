def numbers():
    sum = 2
    previous = 1
    current = 2

    while current < 4000000:
        combined = previous + current
        previous = current
        current = combined

        if current % 2 == 0:
            sum += current

    print(sum)

numbers()