# Sistema de Login - Kivy

Sistema de autenticação completo desenvolvido em Python usando Kivy para interface gráfica e SQLite para banco de dados.

## 📋 Funcionalidades

- **Cadastro de usuários** com validação de dados
- **Login seguro** com verificação de credenciais
- **Tela principal** exibindo informações do usuário logado
- **Banco de dados SQLite** para persistência de dados
- **Interface responsiva** com Kivy

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Kivy** - Framework para interface gráfica
- **SQLite3** - Banco de dados local
- **Arquitetura MVC** - Separação de responsabilidades

## 🎯 Metodologias de Desenvolvimento

Este projeto foi desenvolvido seguindo as melhores práticas de programação:

### Programação Orientada a Objetos (POO)
- **Encapsulamento**: Métodos privados e proteção de dados sensíveis
- **Herança**: Classes filhas herdam funcionalidades das classes pai
- **Polimorfismo**: Métodos sobrescritos para comportamentos específicos
- **Abstração**: Separação clara entre interface e implementação

### Princípios SOLID
- **S** - Single Responsibility: Cada classe tem uma responsabilidade específica
- **O** - Open/Closed: Classes abertas para extensão, fechadas para modificação
- **L** - Liskov Substitution: Classes filhas podem substituir classes pai
- **I** - Interface Segregation: Interfaces específicas e coesas
- **D** - Dependency Inversion: Dependência de abstrações, não de implementações

### Clean Code
- **Nomes descritivos**: Variáveis e métodos com nomes claros
- **Funções pequenas**: Métodos com responsabilidade única
- **Comentários úteis**: Documentação onde necessário
- **Estrutura organizada**: Separação lógica em módulos e pacotes
- **Código legível**: Formatação consistente e padrões de codificação

## 📁 Estrutura do Projeto

```
projeto_login/
├── main.py                     # Arquivo principal
├── construct.kv                # Interface Kivy
├── banco.db                    # Banco de dados SQLite
├── classes/
│   ├── __init__.py
│   ├── classBuildApp.py        # Classe principal da aplicação
│   ├── classDatabase.py        # Gerenciamento do banco de dados
│   ├── classJanelaControle.py  # Controle de telas
│   ├── classJanelaLogin.py     # Tela de login
│   ├── classJanelaCadastro.py  # Tela de cadastro
│   └── classJanelaPrincipal.py # Tela principal
├── imports/
│   ├── __init__.py
│   └── kivy_imports.py         # Importações do Kivy
└── modules/
    ├── __init__.py
    ├── validarEntradas.py      # Validação de formulários
    └── popUp.py                # Mensagens de erro
```

## 🗄️ Banco de Dados

### Tabela: usuario
```sql
CREATE TABLE usuario (
    email TEXT PRIMARY KEY,
    nome TEXT,
    sobrenome TEXT,
    senha TEXT,
    [create] DATE
);
```

## 🔧 Instalação e Execução

### Pré-requisitos
```bash
pip install kivy
```

### Executar o projeto
```bash
python main.py
```

#### Instale o Executável
- Baixe o arquivo .zip na pasta /dist
- Descompacte e execute
O seu sistema operacional pode alertar como um arquivo desconhecido, clique em "Executar mesmo assim" ou semelhante.

## 📱 Telas do Sistema

### 1. Tela de Login
- **Campos**: Email e Senha
- **Botões**: 
  - "Login" - Autentica o usuário
  - "Não tem uma conta? Crie uma" - Navega para cadastro

### 2. Tela de Cadastro
- **Campos**: Nome, Sobrenome, Email e Senha
- **Validações**:
  - Email deve conter "@"
  - Nome/Sobrenome não podem ter números
  - Senha deve ter pelo menos 8 caracteres
- **Botões**:
  - "Salvar" - Cadastra novo usuário
  - "Já possui uma conta? Faça login" - Volta para login

### 3. Tela Principal
- **Exibe**: Nome completo, email e data de criação da conta
- **Botão**: "Sair" - Retorna para tela de login

## 🏗️ Arquitetura

O projeto segue uma arquitetura bem estruturada com separação clara de responsabilidades:

### Classes Principais

#### BuildApp
- Herda de `App` e `Queries`
- Inicializa o banco de dados
- Carrega o arquivo .kv
- Configura as telas do sistema

#### Banco
- Gerencia conexões com SQLite
- Métodos para conectar, desconectar e executar queries

#### Queries
- Herda de `Banco`
- Implementa operações CRUD:
  - `iniciarBanco()` - Cria tabela se não existir
  - `_insert()` - Cadastra novo usuário
  - `_busca()` - Busca dados do usuário
  - `_delete()` - Remove usuário
  - `_update()` - Atualiza dados

#### Telas (Screen)
- **JanelaLogin**: Autenticação de usuários
- **JanelaCadastro**: Registro de novos usuários  
- **JanelaPrincipal**: Dashboard do usuário logado
- **JanelaControle**: Gerenciador de telas (ScreenManager)

## 🔐 Validações Implementadas

### Validação de Email Básica
```python
if '@' not in email:
    return False
```

### Validação de Nome/Sobrenome
```python
if any(char.isdigit() for char in nome):
    return False
```

### Validação de Senha
```python
if len(senha) < 8 or senha.strip() == '':
    return False

if str(senha_banco[0]) == str(senha):
    return True
else:
    return False
```

## 🎨 Interface (Kivy)

### Layouts Utilizados
- **FloatLayout**: Posicionamento absoluto dos elementos
- **pos_hint**: Posicionamento relativo (0.0 a 1.0)
- **size_hint**: Tamanho relativo dos widgets

### Elementos da Interface
- **Label**: Textos e títulos
- **TextInput**: Campos de entrada
- **Button**: Botões de ação
- **Screen**: Telas do aplicativo
- **ScreenManager**: Navegação entre telas

## 🔄 Fluxo da Aplicação

1. **Inicialização**
   - `main.py` instancia `BuildApp`
   - Banco de dados é inicializado
   - Telas são criadas e adicionadas ao ScreenManager

2. **Cadastro**
   - Usuário preenche formulário
   - Dados são validados
   - Se válidos, são inseridos no banco
   - Retorna para tela de login

3. **Login**
   - Usuário insere credenciais
   - Sistema valida no banco de dados
   - Se válido, navega para tela principal
   - `identificador` é definido com o email

4. **Tela Principal**
   - `on_pre_enter` chama método `entrar()`
   - Busca dados do usuário no banco
   - Exibe informações na interface

5. **Logout**
   - Retorna para tela de login
   - Limpa dados da sessão

## 🐛 Tratamento de Erros

### Popups de Erro
- **erroForm()**: Formulário inválido
- **erroLogin()**: Credenciais incorretas

### Validações de Banco
- Verificação de conexão antes de executar queries
- Tratamento de exceções SQL
- Commit automático das transações

## 📝 Exemplo de Uso

```python
# Executar aplicação
from classes import BuildApp

app = BuildApp()
app.run()
```

## 🔮 Possíveis Melhorias

- [ ] Criptografia de senhas (hash)
- [ ] Recuperação de senha
- [ ] Validação de email mais robusta
- [ ] Temas personalizáveis
- [ ] Backup automático do banco
- [ ] Logs de atividade
- [ ] Perfis de usuário
- [ ] Autenticação de dois fatores

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

Projeto desenvolvido para fins educacionais.

## 👨‍💻 Autor

Projeto desenvolvido durante os estudos na Fundação Bradesco.
