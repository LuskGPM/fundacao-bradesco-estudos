from kivy.uix.popup import Popup
from kivy.uix.label import Label

def erroForm():
    pop = Popup(title = 'Formulário Inválido', content = Label(
        text='Preencha todos os campos'
    ), size=(200, 200))
    
def erroLogin():
    Popup(title = 'Invalid Login', content = Label(
        text='Email ou senha inválidos'
    ), size=(300, 300))