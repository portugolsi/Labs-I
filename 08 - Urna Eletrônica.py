sair = False
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
eleitores = int(input())
cont = 0
while (sair == False) :
    voto = input().strip()
    if voto == '1':
        cand1 +=1
        cont+=1
    elif voto == '2':
        cand2 +=1
        cont+=1
    elif voto == '3':
        cand3 +=1
        cont+=1
    elif voto == '4':
        cand4 +=1
        cont+=1
    elif voto == 'sair':
        sair = True
        cont+=1
    else:
        nulo +=1
        cont+=1

    if(cont==eleitores):
        sair = True
    
    
votosValidos = cand1+cand2+cand3+cand4+nulo
Pcand1 = cand1*100/votosValidos
Pcand2 = cand2*100/votosValidos
Pcand3 = cand3*100/votosValidos
Pcand4 = cand4*100/votosValidos
Pnulo = nulo*100/votosValidos

print("""Nome--------------Votos--------------Porcentagem""")
print(f'José Alfredo ------ {cand1} ------------------- {Pcand1:.2f}%')
print(f'Maria Junqueira --- {cand2} ------------------- {Pcand2:.2f}%')
print(f'Marivaldo Silva --- {cand3} ------------------- {Pcand3:.2f}%')
print(f'Juliana Antônia --- {cand4} ------------------- {Pcand4:.2f}%')
print(f'Nulo -------------- {nulo} ------------------- {Pnulo:.2f}%')
