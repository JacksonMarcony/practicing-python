# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hours = float(input("Valor por hora: "))
hoursPerMonth = int(input("Horas por mês: "))

print("Seu salário esse mês será de: ", (hours*hoursPerMonth))