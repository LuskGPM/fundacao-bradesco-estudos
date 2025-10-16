from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def erroForm():
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    layout.add_widget(Label(text='Preencha todos os campos corretamente, a senha deve ter 8 dígitos'))
    
    btn = Button(text='OK', size_hint=(1, 0.3))
    layout.add_widget(btn)
    
    pop = Popup(title='Formulário Inválido', content=layout, 
                size_hint=(0.6, 0.4), auto_dismiss=True)
    btn.bind(on_release=pop.dismiss)
    pop.open()
    
def erroLogin():
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    layout.add_widget(Label(text='Email ou senha inválidos'))
    
    btn = Button(text='OK', size_hint=(1, 0.3))
    layout.add_widget(btn)
    
    pop = Popup(title='Login Inválido', content=layout, 
                size_hint=(0.6, 0.4), auto_dismiss=True)
    btn.bind(on_release=pop.dismiss)
    pop.open()