import datetime
import sqlite3 as sql

class Banco():
    def __init__(self):
        self.__conexao = None
        self.__cursor = None
        self.__conectado = False
    
    def _getConexao(self):
        return self.__conexao
    
    def _getCursor(self):
        return self.__cursor
        
    def _conectar(self):
        self.__conexao = sql.connect('banco.db')
        self.__cursor = self.__conexao.cursor()
        self.__conectado = True
        
    def _disconectar(self):
        self.__conexao.close()
        self.__conectado = False
        
    def _execute(self, sql, parametros = None):
        if self.__conectado:
            if parametros == None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql, parametros)
        else:
            return False
        
    def _fetchAll(self):
        return self.__cursor.fetchall()
    
    def _fetchOne(self):
        return self.__cursor.fetchone()
    
    def _comitar(self):
        try:
            self.__conexao.commit()
        except sql.Error as e:
            print(e)
            return False

class Queries(Banco):
    def __init__(self):
        super().__init__()
        
    def iniciarBanco(self):
        self._conectar()
        self._execute('create table if not exists usuario (email text primary key, nome text, sobrenome text, senha text, [create] date)')
        self._comitar()
        self._disconectar()
        
    def _insert(self, email:str, nome:str, sobrenome:str, senha:str):
        self._conectar()
        date = self._getDate()
        try:
            self._execute('insert into usuario (email ,nome, sobrenome, senha, [create]) values (?, ?, ?, ?, ?)', (
                email.strip(), 
                nome.strip(), 
                sobrenome.strip(), 
                senha.strip(),
                date
                ))
            self._comitar()
        except sql.IntegrityError as e:
            print('Email já cadastrado ', e)
        self._disconectar()
        
    def _busca(self, email:str = '', nome:str = '', sobrenome:str = ''):
        self._conectar()
        self._execute('select nome, sobrenome, [create] from usuario where nome like ? or sobrenome like ? or email = ?', (
            nome.strip().lower(),
            sobrenome.strip().lower(),
            email.strip().lower(),
            ))
        dados = self._fetchAll()
        self._disconectar()
        
        lista = list()
        for l in dados:
            for i in l:
                lista.append(i)
                
        print(lista)
        return lista
        
    def _delete(self, email:str):
        self._conectar()
        self._execute('delete from usuario where email = ?', (email,))
        self._comitar()
        self._disconectar()
        
    def _update(self, email:str, nome:str, sobrenome:str, senha:str):
            self._conectar()
            self._execute('update usuario set nome = ?, sobrenome = ?, senha = ? where email = ?', (nome, sobrenome, senha, email))
            self._comitar()
            self._disconectar()
    
    def _validarSenha(self, senha:str, email:str):
        self._conectar()
        self._execute('select senha from usuario where email = ?', (email,))
        senha_banco = self._fetchOne()
        self._disconectar()
        if str(senha_banco[0]) == str(senha):
            return True
        else:
            return False
    
    @staticmethod
    def _getDate():
        return str(datetime.datetime.now()).split(' ')[0]
    