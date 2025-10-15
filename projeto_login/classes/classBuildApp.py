from imports import App, Builder
from .classJanelaControle import JanelaControle
from .classJanelaLogin import JanelaLogin
from .classJanelaPrincipal import JanelaPrincipal
from .classJanelaCadastro import JanelaCadastro

## Variáveis Globais

class BuildApp(App):
    exe = JanelaControle()
    kv = Builder.load_file('construct.kv')
    screens = [JanelaLogin(name='login'), JanelaCadastro(name = 'cadastro'), JanelaPrincipal(name = 'principal')]
        
    def build(self):
        for s in self.screens:
            self.exe.add_widget(s)
        
        self.kv
        self.exe.current = 'login'
        return self.exe
    