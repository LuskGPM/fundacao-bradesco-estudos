def validarEntradas(nome:str, sobrenome:str, email:str, cpf:str) -> bool:
    
    if any(char.isdigit() for char in nome) or any(char.isdigit() for char in sobrenome):
        print('Nome ou sobrenome não pode conter números')
        return False
    
    elif '@' not in email:
        print('Email inválido')
        return False
    
    else:
        return True
