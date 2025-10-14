from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from .database import Queries
from .functions import *


class JanelaCriarConta(Screen, Queries):
    nome = ObjectProperty(None)
    sobrenome = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
       
    def reset(self):
        self.nome.text=''
        self.sobrenome.text=''
        self.email.text=''
        self.senha.text=''
        
    def _salvar(self):
        if validarEntradas(self.nome, self.sobrenome, self.email): 
            self._insert(
                nome=self.nome.text,
                sobrenome=self.sobrenome.text,
                email = self.email.text,
                senha = self.senha.text
            )
            self.__reset()
            
        else:
            invalidForm()
            
class JanelaControle(ScreenManager):
    pass

class JanelaLogin(Screen, Queries):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    
    def _loginBtn(self):
        if validarEntradas(email=self.email, senha=self.senha):
            JanelaPrincipal.atual = self.email.text
            self.reset()
            jc.current = 'main'
        else:
            invalidLogin()
    
    def createBtn(self):
        self.reset()
        jc.current = 'create'
        
    def reset(self):
        self.email.text=''
        self.senha.text=''
            
class JanelaPrincipal(Screen, Queries):
    
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    atual = ''
    
    def logOut(self):
        jc.current = 'login'
    
    def entrar(self):
        senha, nome, created = self._search(email=self.atual)
        
        self.n.text=f'Nome da Conta: {nome}'
        self.email.text=f'Email: {self.atual}'
        self.created.text=f'Criado em: {created}'
        
class BuildApp(App):
    global jc, kv, screens
    jc = JanelaControle()
    kv = Builder.load_file('construtor.kv')
    screens = [JanelaLogin(name='login'), JanelaCriarConta(name = 'create'), JanelaPrincipal(name = 'main')]
    
    def build(self):
        for Screen in screens:
            jc.add_widget(Screen)
        
        jc.current = 'login'
        
        return jc