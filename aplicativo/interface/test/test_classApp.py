from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.red = [1,0,0,1]
        self.green = [0,1,0,1]
        self.blue = [0,0,1,1]
        self.purple = [1,0,1,1]
        
    def build(self):
        
        label = Label(
            text='Olá, Mundo!',
            size_hint = (.5, .5),
            pos_hint = {
                'center_x': .5,
                'center_y': .5
            }
            )
        image = AsyncImage(
            source='https://supermariorun.com/assets/img/stage/mario03.png',
            size_hint = (.5, .5),
            pos_hint = {
                'center_x':.5,
                'center_y':.5
            }
            )
        
        layout = BoxLayout(padding = 10, spacing = 10, orientation = 'vertical')
        cores = [self.red, self.green, self.blue, self.purple]
        
        for i, cor in enumerate(cores):
            
            btn = Button(text = f'Botão {i+1}',
                         background_color=cor)
            layout.add_widget(btn)
            
        botao = Button(
            text='Pressione',
            size_hint=(.1, .1),
            pos_hint={'x': .5, 'y': .5}
        )
        botao.bind(on_press=self.pressionarButton)
        
        return botao
    
    def pressionarButton(self, instance):
        print('Você pressionou o botão')


class ButtonMain(App):
    def build(self):
        return Button()
    
    def on_press_button(self):
        print('Pressionar Botão')
        
    