n1 = float(input('nota 1'))
n2 = float(input('nota 2'))
media = (n1 + n2)/2
print('A media é:', media )
if media == 10:
    print('aprovado')
elif media >= 7:
    print('Aprovado com Distinção')
elif media < 7:
    print('reprovado')
