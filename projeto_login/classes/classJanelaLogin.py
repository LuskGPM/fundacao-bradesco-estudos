from imports import Screen, ObjectProperty
from modules import validarEntradas, erroLogin
from .classJanelaPrincipal import JanelaPrincipal

class JanelaLogin(Screen):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
        
    def btnLogin(self):
        if validarEntradas(email=self.email.text, senha=self.senha.text):
            JanelaPrincipal.identificador = self.email.text
            self.manager.current = 'principal'
            self.reset()
            
        else:
            erroLogin()
            
    def btnCadastro(self):
        self.reset()
        self.manager.current = 'cadastro'
            
    def reset(self):
        self.email.text=''
        self.senha.text=''
        