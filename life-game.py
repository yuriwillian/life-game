usuario = "admin"
senha = "123"

def criarConta():
    print("Crie uma conta no Life Game para começar a jogar\n")
    usuario = input("Digite o nome de usuario desejado:\n-->")
    senha = input("Digite uma senha:\n-->")
    repeteSenha = input("Repita a senha digitada:\n-->")
    while (senha != repeteSenha):
        print("As senhas não são iguais! Tente novamente.\n")
        senha = input("Digite uma senha:\n-->")
        repeteSenha = input("Repita a senha digitada:\n-->")
    print("Conta criada com sucesso!")
    validaLogin() # não ta funcionando...
def startGame():
    def richLife():
        print("Você é herdeiro!")
    
    def poorLife():
        print("Você nasceu pobre :(")

    rico = input("Deseja nascer em familia rica? Digite 's' ou 'n'\n-->")
    if(rico == "s"):
        richLife()
    elif(rico == "n"):
        poorLife()

def validaLogin():
    print("Faça login para jogar o Life Game\n")
    usuarioDigitado = input("Digite seu nome de usuario:\n-->")
    senhaDigitada = input("Digite sua senha:\n-->")
    while(usuarioDigitado != usuario and senhaDigitada != senha):
        print("Usuario ou senha invalidos!\n-->")
        validaLogin()
    print("Usuario e senha corretos :)")
    startGame()

def inicio():
    print("----------LIFE GAME----------")
    beginner = input("Possui uma conta? Digite 's' ou 'n':\n-->")
    if(beginner == "s"):
        validaLogin()
    elif(beginner == "n"):
        criarConta()
    else:
        inicio()


inicio()