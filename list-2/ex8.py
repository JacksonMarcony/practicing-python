p1 = int(input('Entre com o preço do primeiro produto'))
p2 = int(input('Entre com o preço do segundo produto'))
p3 = int(input('Entre com o preço do terceiro produto'))

if p1 < p2 and p1 < p3:
    best = p1
    msg = f'compre o{best}'
elif p2 < p1 and p2 < p3:
    best = p2
    msg = f'compre o{best}'
elif p3 < p2 and p3 < p1:
    best = p3
    msg = f'compre o{best}'
print(msg)