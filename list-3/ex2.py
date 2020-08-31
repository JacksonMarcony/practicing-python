user = input('Digite user')
senha = input('Digite senha')
if user == senha:
    while True:
        print("user e senha nao podem ser iguais")
        user = input('Digite user ')
        senha = input('Digite senha')
        if user != senha:
            break