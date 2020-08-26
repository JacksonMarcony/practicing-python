#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal,
#  utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: ((62.1*h) - 44.7)

height = float(input("peso: "))
sex = str(input("m ou f "))

if (sex == "m"):
    print('peso ideal:', ((72.7 * height) - 58))
elif (sex == "f"):
    print('peso ideal:', ((62.1 * height) - 44.7))