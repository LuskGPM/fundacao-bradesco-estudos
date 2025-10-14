from kivy.uix.popup import Popup
from kivy.uix.label import Label

def validarEntradas(nome:str = '', sobrenome:str = '', email:str = '', senha:str = '') -> bool:
    
    if any(char.isdigit() for char in nome) or any(char.isdigit() for char in sobrenome):
        print('Nome ou sobrenome não pode conter números')
        return False
    
    elif '@' not in email:
        print('Email inválido')
        return False
    
    if len(senha) == 0 or senha.strip == '':
        return False
    
    else:
        return True

def invalidForm():
    popup = Popup(title = 'Invalid Form', content = Label(
        text='Preencha todos os campos'
    ), size=(400, 400))
    popup.open()
      
def invalidLogin():
    popup = Popup(title = 'Invalid Login', content = Label(
        text='Usuário ou senha inválidos'
    ), size=(400, 400))
    popup.open()