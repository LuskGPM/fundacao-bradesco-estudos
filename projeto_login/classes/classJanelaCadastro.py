from imports import Screen, ObjectProperty
from modules import validarEntradas, erroForm
from .classDatabase import Queries
from .classJanelaControle import JanelaControle

class JanelaCadastro(Screen, Queries):
    email = ObjectProperty(None)
    nome = ObjectProperty(None)
    sobrenome = ObjectProperty(None)
    senha = ObjectProperty(None)
    exe = JanelaControle()
    
    def reset(self):
        self.email.text=''
        self.nome.text=''
        self.sobrenome.text=''
        self.senha.text=''
    
    def login(self):
        self.reset()
        self.exe.current = 'login'
        
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
            
