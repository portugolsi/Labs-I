sair = False

while sair == False:
    validador = 0
    senha = input().strip()
    confSenha = input().strip()
    for l in senha:
        if l.isupper():
            validador +=1
    if validador == 0:
        print('Senha inválida')
        
    else:
        if (senha == confSenha):
            if len(senha)>=7 and len(senha)<=8:
                print('Senha válida')
                sair = True
            else:
                print('Senha inválida')
    
        else:
            print('Senha inválida')
