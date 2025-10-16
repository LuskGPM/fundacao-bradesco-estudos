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
        
    def login(self):
        self.reset()
        jc.current = 'login'
        
    def submit(self):
        if validarEntradas(self.nome.text, self.sobrenome.text, self.email.text, self.senha.text): 
            self._insert(
                nome=self.nome.text,
                sobrenome=self.sobrenome.text,
                email = self.email.text,
                senha = self.senha.text
            )
            self.reset()
            
            
            
        else:
            print('erro aqui')
            invalidForm()
            
class JanelaControle(ScreenManager):
    pass

class JanelaLogin(Screen, Queries):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    
    def loginBtn(self):
        if validarEntradas(email=self.email.text, senha=self.senha.text):
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
    email = ObjectProperty(None)
    atual = ''
    
    def on_pre_enter(self, *args):
        return self.entrar()
    
    def logOut(self):
        jc.current = 'login'
    
    def entrar(self):
        dados = self._search(email=self.atual)
        nome = dados[1]
        sobrenome = dados[2]
        
        self.n.text=f'Nome da Conta: {nome} {sobrenome}'
        self.email.text=f'Email: {self.atual}'
        
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