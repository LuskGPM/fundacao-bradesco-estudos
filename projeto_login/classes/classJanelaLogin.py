from imports import Screen, ObjectProperty
from modules import validarEntradas, erroLogin
from .classJanelaPrincipal import JanelaPrincipal
from .classDatabase import Queries

class JanelaLogin(Screen, Queries):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
        
    def btnLogin(self):
        if validarEntradas(email=self.email.text, senha=self.senha.text, login=True):
            print(f'Validar entradas {self.email.text}')
            if self._busca(email=self.email.text):
                print('Busca Usuario')
                if self._validarSenha(senha=self.senha.text, email=self.email.text):
                    print('Validou a senha')
                    JanelaPrincipal.identificador = self.email.text
                    self.manager.current = 'principal'
                    self.reset()
                else:
                    erroLogin()
            else:
                erroLogin()
        else:
            erroLogin()
            
    def btnCadastro(self):
        self.reset()
        self.manager.current = 'cadastro'
            
    def reset(self):
        self.email.text=''
        self.senha.text=''
        