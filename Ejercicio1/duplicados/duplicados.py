def eliminar_duplicados(lista):
    lista_nueva = []
    for x in lista:
        if x not in lista_nueva:
            lista_nueva.append(x)

    return lista_nueva


lista = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 7]
print(eliminar_duplicados(lista))
