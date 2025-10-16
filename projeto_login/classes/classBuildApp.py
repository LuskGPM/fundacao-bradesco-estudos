from imports import Builder, App
from .classJanelaControle import JanelaControle
from .classJanelaLogin import JanelaLogin      
from .classJanelaCadastro import JanelaCadastro  
from .classJanelaPrincipal import JanelaPrincipal
from .classDatabase import Queries

class BuildApp(App, Queries):
    
    def build(self):
        self.iniciarBanco()
        Builder.load_file('construct.kv')
        screens = [JanelaLogin(name = 'login'), JanelaCadastro(name = 'cadastro'), JanelaPrincipal(name = 'principal')]
        sm = JanelaControle()
        for s in screens:
            sm.add_widget(s)
        return sm