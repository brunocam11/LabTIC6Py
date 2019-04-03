def divisores(num):
    divisores_num = [x for x in range(1, num) if num % x == 0]
    return divisores_num


print(divisores(7))
