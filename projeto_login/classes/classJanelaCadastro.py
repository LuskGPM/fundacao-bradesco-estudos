from imports import Screen, ObjectProperty
from modules import validarEntradas, erroForm
from .classDatabase import Queries

class JanelaCadastro(Screen, Queries):
    email = ObjectProperty(None)
    nome = ObjectProperty(None)
    sobrenome = ObjectProperty(None)
    senha = ObjectProperty(None)
    
    def reset(self):
        self.email.text=''
        self.nome.text=''
        self.sobrenome.text=''
        self.senha.text=''
        self.manager.current = 'login'
    
    def login(self):
        self.reset()
        self.manager.current = 'login'
        
    def submit(self):
        if validarEntradas(
            email=self.email.text,
            nome=self.nome.text,
            sobrenome=self.sobrenome.text,
            senha=self.senha.text
        ):
            self._insert(
                email=self.email.text,
                nome=self.nome.text,
                sobrenome=self.sobrenome.text,
                senha=self.senha.text
            )
            self.reset()
            
        else:
            erroForm()
            
