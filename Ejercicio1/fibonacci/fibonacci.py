def fibonacci(n):
    num_list = []

    for num in range(0, n):
        if num == 0 or num == 1:
            num_list.append(num)
        else:
            num_to_add = num_list[num-1] + num_list[num-2]
            num_list.append(num_to_add)

    return num_list


print(fibonacci(10))
