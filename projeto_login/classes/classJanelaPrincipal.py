from imports import ObjectProperty, Screen
from .classDatabase import Queries
from modules import erroLogin

class JanelaPrincipal(Screen, Queries):
    n = ObjectProperty(None)
    create = ObjectProperty(None)
    email_label = ObjectProperty(None)
    identificador = ''
    
    def on_pre_enter(self, *args):
        self.entrar()
        
    def logout(self):
        self.manager.current = 'login'
        
    def btnDelete(self):
        self._delete(email=self.identificador)
        self.manager.current = 'login'
        
    def entrar(self):
        dados = self._busca(email=self.identificador)
        
        if len(dados) == 0:
            self.logout()
        else:
            self.n.text = f'Nome completo: {dados[0]} {dados[1]}'
            self.email_label.text = f'Email: {self.identificador}'
            self.create.text = f'Criado em: {dados[-1]}'

            