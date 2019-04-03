def list_comp(list):
    list_pares = [x for x in list if x % 2 == 0]
    return list_pares


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(list_comp(a))
