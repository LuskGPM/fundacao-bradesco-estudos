from imports import ObjectProperty, Screen
from .classDatabase import Queries
from .classJanelaControle import JanelaControle

class JanelaPrincipal(Screen, Queries):
    nome_completo = ObjectProperty(None)
    create = ObjectProperty(None)
    email = ObjectProperty(None)
    identificador = ''
    
    def __init__(self):
        self.exe = JanelaControle()
    
    def on_pre_enter(self, *args):
        self.entrar()
        
    def logout(self):
        self.exe.current = 'login'
        
    def entrar(self):
        dados = self._busca(email=self.identificador)
        self.nome_completo.text=f'Usuário {dados[0]} {dados[1]}'
        self.email.text=f'Email: {self.identificador}'
        self.create.text=f'Criado em: {dados[-1]}'

            