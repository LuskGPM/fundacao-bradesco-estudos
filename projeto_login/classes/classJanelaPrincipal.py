from imports import ObjectProperty, Screen
from .classDatabase import Queries

class JanelaPrincipal(Screen, Queries):
    n = ObjectProperty(None)
    create = ObjectProperty(None)
    email_label = ObjectProperty(None)
    identificador = ''
    
    def on_pre_enter(self, *args):
        self.entrar()
        
    def logout(self):
        self.manager.current = 'login'
        
    def entrar(self):
        dados = self._busca(email=self.identificador)
        self.n.text = f'Nome completo: {dados[0]} {dados[1]}'
        self.email_label.text = 'Email: ',self.identificador
        self.create.text = 'Criado em: ',str(dados[-1])

            