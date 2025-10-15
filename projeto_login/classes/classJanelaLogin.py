from imports import Screen, ObjectProperty
from modules import validarEntradas, erroLogin
from .classJanelaControle import JanelaControle
from .classJanelaPrincipal import JanelaPrincipal

class JanelaLogin(Screen):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    
    def __init__(self):
        self.exe = JanelaControle()
        
    def btnLogin(self):
        if validarEntradas(email=self.email.text, senha=self.senha.text):
            JanelaPrincipal.identificador = self.email.text
            self.exe.current = 'main'
            self.reset()
            
        else:
            erroLogin()
            
    def btnCadastro(self):
        self.reset()
        self.exe.current = 'cadastro'
            
    def reset(self):
        self.email.text=''
        self.senha.text=''
        