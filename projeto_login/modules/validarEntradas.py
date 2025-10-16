def validarEntradas(
    email:str = '',
    nome:str = '',
    sobrenome:str = '',
    senha:str = ''
    ) -> bool:
    
    if '@' not in email:
        print(f'Email incorreto: {email}')
        return False
    
    elif any(char.isdigit() for char in nome) or any(char.isdigit() for char in sobrenome):
        print(f'Nome ou sobrenome não pode conter números: {nome}')
        return False
    
    elif len(senha) < 8 or senha.strip() == '':
        print(f'Senha vazia ou menor que 8 dígitos: {senha}')
        return False
    
    return True