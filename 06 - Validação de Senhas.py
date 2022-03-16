senha = input()
confSenha = input()
if len(senha)>3 and len(senha)<9:
    if senha==confSenha:
        print('Senha válida')
    else:
        print('Senha inválida')
else:
    print('Senha inválida')
