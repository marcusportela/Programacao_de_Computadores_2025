from PyQt5 import QtWidgets, QtGui, QtCore
import re
import random
import string

# Function to check password strength
def senha_forte(senha):
    return (
        len(senha) >= 8
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(c in "!@#$%^&*()-_=+" for c in senha)
    )

# Function to generate a strong password
def gerar_senha():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(random.choice(caracteres) for _ in range(12))

usuarios = {}

class TelaInicial(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: black; color: white;")
        
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label = QtWidgets.QLabel("Bem-vindo!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        
        button_style = "background: rgba(255, 255, 255, 0.3); border: 2px solid rgba(255, 255, 255, 0.5); border-radius: 10px; padding: 5px; color: white;"
        
        self.cadastro_button = QtWidgets.QPushButton("Cadastro")
        self.cadastro_button.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.cadastro_button.setStyleSheet(button_style)
        self.cadastro_button.clicked.connect(self.abrir_cadastro)
        
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.login_button.setStyleSheet(button_style)
        self.login_button.clicked.connect(self.abrir_login)
        
        layout.addWidget(self.label)
        layout.addWidget(self.cadastro_button)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
    
    def abrir_cadastro(self):
        self.cadastro_screen = CadastroScreen()
        self.cadastro_screen.show()
        self.close()
    
    def abrir_login(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()
        self.close()

class CadastroScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: black; color: white;")
        
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label = QtWidgets.QLabel("Cadastro de Usuário")
        self.label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.user_input = QtWidgets.QLineEdit()
        self.pass_input = QtWidgets.QLineEdit()
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.sugestao_input = QtWidgets.QLineEdit()
        self.sugestao_input.setReadOnly(True)
        self.sugestao_input.setVisible(False)
        
        button_style = "background: rgba(255, 255, 255, 0.3); border: 2px solid rgba(255, 255, 255, 0.5); border-radius: 10px; padding: 5px; color: white;"
        
        self.cadastro_button = QtWidgets.QPushButton("Cadastrar")
        self.cadastro_button.setStyleSheet(button_style)
        self.cadastro_button.clicked.connect(self.cadastrar)
        
        layout.addWidget(self.label)
        layout.addWidget(QtWidgets.QLabel("Escolha um nome de usuário"))
        layout.addWidget(self.user_input)
        layout.addWidget(QtWidgets.QLabel("Crie a senha"))
        layout.addWidget(self.pass_input)
        layout.addWidget(self.sugestao_input)
        layout.addWidget(self.cadastro_button)
        
        self.setLayout(layout)
    
    def cadastrar(self):
        usuario = self.user_input.text()
        senha = self.pass_input.text()
        
        if senha_forte(senha):
            usuarios[usuario] = senha
            QtWidgets.QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso!")
            self.login_screen = LoginScreen()
            self.login_screen.show()
            self.close()
        else:
            self.show_sugestao_popup()
    
    def show_sugestao_popup(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Erro!")
        msg_box.setText("Sua senha é fraca! Gostaria da sugestão de uma senha forte?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        resposta = msg_box.exec_()
        
        if resposta == QtWidgets.QMessageBox.Yes:
            self.sugestao_input.setText(f"Sugestão de senha: {gerar_senha()}")
            self.sugestao_input.setVisible(True)

class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: black; color: white;")
        
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label = QtWidgets.QLabel("Login")
        self.label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.user_input = QtWidgets.QLineEdit()
        self.pass_input = QtWidgets.QLineEdit()
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        button_style = "background: rgba(255, 255, 255, 0.3); border: 2px solid rgba(255, 255, 255, 0.5); border-radius: 10px; padding: 5px; color: white;"
        
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.setStyleSheet(button_style)
        self.login_button.clicked.connect(self.login)
        
        self.cadastro_button = QtWidgets.QPushButton("Ainda não tem cadastro? Cadastre-se")
        self.cadastro_button.setStyleSheet(button_style)
        self.cadastro_button.clicked.connect(self.abrir_cadastro)
        
        layout.addWidget(self.label)
        layout.addWidget(QtWidgets.QLabel("Usuário"))
        layout.addWidget(self.user_input)
        layout.addWidget(QtWidgets.QLabel("Senha"))
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cadastro_button)
        
        self.setLayout(layout)
    
    def login(self):
        usuario = self.user_input.text()
        senha = self.pass_input.text()
        if usuarios.get(usuario) == senha:
            QtWidgets.QMessageBox.information(self, "Login", "Login bem-sucedido!")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!")
    
    def abrir_cadastro(self):
        self.cadastro_screen = CadastroScreen()
        self.cadastro_screen.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
