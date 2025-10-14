from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.operadores = ['+', '-', '*', '/']
        self.last_operador = None
        self.last_button = None
        main_layout = BoxLayout(orientation='vertical')
        self.solucao = TextInput(
            multiline = False, readonly = True, halign = 'right', font_size=55
        )
        main_layout.add_widget(self.solucao)
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '+'],
            ['.', '0', 'C', '-']
        ]
        
        for row in botoes:
            h_layout = BoxLayout()
            for label in row:
                btn = Button(
                    text=label,
                    pos_hint={'x':.2 , 'y':.2 }
                )
                btn.bind(on_press=self.on_press_button)
                h_layout.add_widget(btn)
            main_layout.add_widget(h_layout)
        
        equal_button = Button(
            text='=',
            pos_hint={'x':.5 , 'y':.5 }
        ) 
        equal_button.bind(on_press=self.on_press_equal)
        main_layout.add_widget(equal_button)
        
        return main_layout
    
    def on_press_button(self, instance):
        current = self.solucao.text
        botao_text = instance.text
        
        if botao_text == 'C':
            self.solucao.text = ''
            
        else:
            if current and self.last_operador and botao_text in self.operadores:
                
                return
            
            elif current == '' and botao_text in self.operadores:
                return
            
            else: 
                new_text = current + botao_text
                self.solucao.text = new_text
            
            self.last_button = botao_text
            self.last_operador = self.last_button in self.operadores
    
    def on_press_equal(self, instance):
        text = self.solucao.text
        if text:
            solution = str(eval(self.solucao.text))
            self.solucao.text = solution
            