idade = int(input())
analfabeto = input()

if (idade>18 and idade<70):
    if analfabeto=='n':
        print('Voto obrigatório')
    else:
        print('Voto não obrigatório')
else:
    print('Voto não obrigatório')
