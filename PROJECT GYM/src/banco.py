import sqlite3

class BancoDeDados(): #DAO significa == 'Data acess object'
    def __init__ (self, db_name='academia.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.criar_tabela()
        print("Banco de dados conectado com sucesso!")

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                telefone TEXT,
                data_matricula TEXT,
                vencimento TEXT
                )
        ''')
        self.conn.commit()


    def cadastrar_aluno(self, aluno):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO alunos (nome, cpf, telefone, data_matricula, vencimento)
            VALUES (?, ?, ?, ?, ?)
    ''', (
        aluno.nome,
        aluno.cpf,
        aluno.telefone,
        aluno.data_matricula,
        aluno.vencimento,
    ))
        self.conn.commit()


    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM alunos')
        return cursor.fetchall()
    
    def buscar_cpf(self, cpf):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM alunos WHERE cpf = ?', (cpf,))
        return cursor.fetchone()
    
    def atualizar_alunos(self, cpf, nome, telefone, data_matricula, vencimento):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE alunos
            SET nome = ?, telefone = ?, data_matricula = ?, vencimento = ?
            WHERE cpf = ?
    ''', (nome, telefone, data_matricula, vencimento, cpf))
        self.conn.commit()
        

    def deletar_aluno(self, cpf):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM alunos WHERE cpf = ?', (cpf,))
        self.conn.commit()
        
