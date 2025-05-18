def squared_sums():
    sum = 0
    sum__for_squared = 0
    for i in range(101):
        sum += i * i
        sum__for_squared += i
    print(sum__for_squared*sum__for_squared-sum)

squared_sums()