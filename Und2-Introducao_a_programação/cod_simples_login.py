# Importação de bibliotecas
import random
import string

# Função para verificar a qualidade de segurança da senha
def senha_forte(senha):
    return (
        len(senha) >= 8
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(c in "!@#$%^&*()-_=+" for c in senha)
    )

# Função para gerar uma senha forte
def gerar_senha():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(random.choice(caracteres) for _ in range(12))

usuarios = {}

# Função para cadastro do usuário
def cadastrar():
    usuario = input("Escolha um nome de usuário: ")
    while True:
        senha = input("Crie uma senha forte: ")
        if senha_forte(senha):
            print("Senha forte! Cadastro realizado com sucesso.")
            usuarios[usuario] = senha
            break
        else:
            print("Senha fraca! Sua senha deve ter pelo menos 8 caracteres, incluir maiúsculas, minúsculas, números e símbolos.")
            opcao = input("Deseja uma sugestão de senha forte? (s/n): ").strip().lower()
            if opcao == 's':
                sugestao = gerar_senha()
                print(f"Sugestão de senha: {sugestao}")

# Função de login
def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuarios.get(usuario) == senha:
        print("Login bem-sucedido! Sua conta está protegida porque sua senha é forte.")
    else:
        print("Usuário ou senha incorretos!")

# Função para controle de menu
while True:
    opcao = input("Você tem login ou deseja se cadastrar? (login/cadastro/sair): ").strip().lower()
    if opcao == "cadastro":
        cadastrar()
    elif opcao == "login":
        login()
    elif opcao == "sair":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")