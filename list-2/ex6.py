num1 = int(input('primeiro numero'))
num2 = int(input('segundo numero'))
num3 = int(input('terceiro numero'))

if num1 > num2 and num1 > num3:
    Maior = num1
elif num2 > num1 and num2 > num3:
    Maior = num2
elif num3 > num2 and num3 > num1:
    Maior = num3
print(Maior)