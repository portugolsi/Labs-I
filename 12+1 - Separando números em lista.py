div = 6 #Coloquei um valor par qualquer aqui só para garantir que ele é um número par e vai entrar no laço:
ini = int(input().strip())
fin = int(input().strip())
while div%2==0:
    div = int(input().strip())

primos = []
pares = []
divisiveis = []
cont = 0
for k in range(ini,fin):

    for numero in range(2,k):
        if k%numero==0:
            cont=cont+1
    if cont==0:
        primos.append(k)
    cont = 0
    if k%2==0:
        pares.append(k)
    if k%div==0:
        divisiveis.append(k)
print(primos)
print(pares)
print(divisiveis)

