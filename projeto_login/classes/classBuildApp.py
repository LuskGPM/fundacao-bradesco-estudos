import os
import sys
from imports import Builder, App
from .classJanelaControle import JanelaControle
from .classJanelaLogin import JanelaLogin      
from .classJanelaCadastro import JanelaCadastro  
from .classJanelaPrincipal import JanelaPrincipal
from .classDatabase import Queries

class BuildApp(App, Queries):
    
    def build(self):
        self.iniciarBanco()
        
        # Caminho correto para o arquivo .kv (funciona com PyInstaller)
        if getattr(sys, 'frozen', False):
            # Executável do PyInstaller
            base_path = sys._MEIPASS
        else:
            # Desenvolvimento
            base_path = os.path.dirname(os.path.abspath(__file__))
            base_path = os.path.dirname(base_path)  # Volta um diretório
        
        kv_path = os.path.join(base_path, 'construct.kv')
        Builder.load_file(kv_path)
        
        screens = [JanelaLogin(name = 'login'), JanelaCadastro(name = 'cadastro'), JanelaPrincipal(name = 'principal')]
        sm = JanelaControle()
        for s in screens:
            sm.add_widget(s)
        return sm