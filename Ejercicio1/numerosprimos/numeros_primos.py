from divisores.divisores import divisores


def es_primo(num):
    primo = False
    divs = divisores(num)

    if len(divs) == 1:
        primo = True

    return primo


print(es_primo(11))
