#tratamento de erro para uma String
while True:
    nome = input("nome:").strip()
    if not nome:
        print('erro')
    elif nome.replace(' ', '').isalpha():
        break
    else:
        print('erro')
print(nome)
