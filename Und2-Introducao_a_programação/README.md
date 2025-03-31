# Cadastro de Usuários com PyQt5

Este é um aplicativo simples de cadastro e login desenvolvido com **PyQt5**. Ele permite que os usuários se registrem, recebam sugestões de senha forte e façam login no sistema.

## 📌 Funcionalidades
- Interface gráfica com PyQt5.
- Cadastro de usuários com validação de senha forte.
- Sugestão automática de senha caso a senha criada seja fraca.
- Opção para o usuário inserir uma nova senha caso rejeite a sugestão.
- Tela de login para autenticação.

## 🛠️ Requisitos
Antes de executar o código, certifique-se de ter o **Python 3** instalado. Além disso, instale as dependências necessárias:

```bash
pip install PyQt5
```

## 🚀 Como executar
1. Clone este repositório ou copie os arquivos para o seu computador.
2. Renomeie o arquivo para **README.md**.
3. Execute o código com o seguinte comando:
   
   ```bash
   python nome_do_arquivo.py
   ```

4. A interface gráfica será aberta, permitindo que você cadastre e faça login.

## 🔑 Regras para Senha Forte
O sistema considera uma senha forte quando:
- Possui no mínimo **8 caracteres**.
- Contém **letras maiúsculas e minúsculas**.
- Inclui **números**.
- Tem **caracteres especiais** como `!@#$%^&*()-_=+`.

Se a senha for fraca, o sistema sugere uma nova senha segura e dá a opção de digitá-la novamente.
