def verify_card_number(card_number):
    card_number = str(card_number)
    lista = []
    for i in card_number:
        if i.isdigit():
            lista.append(int(i))     
    lista.reverse()
    for i in range(len(lista)):
        if i % 2 == 1:
            lista[i] = lista[i] * 2
            if  lista[i] > 9:
                lista[i] = lista[i] - 9
    if sum(lista) % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"