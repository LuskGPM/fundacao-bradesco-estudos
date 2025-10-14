from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.input = TextInput(
            multiline = False, readonly = True, halign = 'right', font_size=55
        )
        self.btns = self.botoesMetodo()
        self.operadores = self.operadoresMetodo()
        self.ultimo_botao = None
        self.ultimo_caractere = None
    
    def build(self):
        self.construtorLayout()
        return self.layout
    
    def on_press_btn(self, instance):
            valorInput = self.input.text
            textoBotao = instance.text
            
            if textoBotao == 'C':
                self.input.text = ''
                
            else:    
                if self.validarCampoInput(valorInput=valorInput, textoBotao=textoBotao):
                    novoTexto = valorInput + textoBotao
                    self.input.text = novoTexto
            
                self.ultimo_botao = textoBotao
                self.ultimo_caractere = textoBotao in self.operadores
        
    def on_equal(self, instance):
        valorInput = self.input.text
        if valorInput: 
            solucao = str(eval(self.input.text))
            self.input.text = solucao
    
    def validarCampoInput(self, valorInput = None, textoBotao = None):
        if self.ultimo_caractere and textoBotao in self.operadores:
            return False
        
        elif valorInput == '' and textoBotao in self.operadores:
            return False
        
        return True
    
    @staticmethod
    def operadoresMetodo() -> list:
        return ['/', '*', '+', '-']
    
    @staticmethod
    def botoesMetodo() -> list:
        return [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        
    def construtorLayout(self):
        self.layout.add_widget(self.input)
        for linhas in self.btns:
            layout_h = BoxLayout()
            for label in linhas:
                buttons = Button(text = label, font_size=40)
                buttons.bind(on_press=self.on_press_btn)
                layout_h.add_widget(buttons)
            self.layout.add_widget(layout_h)

        botao_igual = Button(text='=', font_size=40)
        botao_igual.bind(on_press=self.on_equal)
        self.layout.add_widget(botao_igual)
