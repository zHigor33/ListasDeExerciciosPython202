print("Cadastro de senha")
username = str(input("Informe um nome de usuário: "))
verifyPassword = True

while verifyPassword:
    password = str(input("Informe uma senha: "))

    if password == username:
        print("Senha não pode ser o nome de usuário")
    
    else:
        verifyPassword = False

print("\nRealize o login")
verifyLogin = True

while verifyLogin:
    loginUsername = str(input("Informe o usuário registrado: "))
    loginPassword = str(input("Informe a senha registrada: "))

    if loginUsername == username:
        if loginPassword == password:
            print("Login efetuado com sucesso!")
            verifyLogin = False
        
        else:
            print("Senha errada")
    
    else:
        print("Nome de usuário errado")
