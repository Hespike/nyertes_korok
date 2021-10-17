def nyertes_korok(lista1, lista2):
    if len(lista1) != len(lista2) or len(lista1) == 0 or len(lista2) == 0:
        return -1
    nyert = 0
    for x in range(len(lista1)):
        if lista1[x] > lista2[x]:
            nyert = nyert + 1
    return(nyert)
