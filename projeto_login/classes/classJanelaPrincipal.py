from imports import ObjectProperty, Screen
from .classDatabase import Queries

class JanelaPrincipal(Screen, Queries):
    nomeCompleto = ObjectProperty(None)
    create = ObjectProperty(None)
    email = ObjectProperty(None)
    identificador = ''
    
    def on_pre_enter(self, *args):
        self.entrar()
        
    def logout(self):
        self.manager.current = 'login'
        
    def entrar(self):
        dados = self._busca(email=self.identificador)
        self.nomeCompleto.text=f'Usuário {dados[0]} {dados[1]}'
        self.email.text=f'Email: {self.identificador}'
        self.create.text=f'Criado em: {dados[-1]}'

            