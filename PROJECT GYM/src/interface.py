import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from aluno import Aluno
from banco import BancoDeDados

class interfaceAcademia():
    def __init__ (self, janela):
        # Configurações iniciais da janela principal
        self.janela = janela 
        self.janela.title("Sistema de cadastros da academia!")
        self.db = BancoDeDados()  # Inicializa conexão com banco
        self.janela.geometry("800x600")

        # ==============================
        #   ESTILOS DO TREEVIEW
        # ==============================
        treeview_style = ttk.Style()
        treeview_style.theme_use("default")

        # Estilo visual do Treeview
        treeview_style.configure("Treeview",
                                 background="#444455",
                                 foreground="white",
                                 fieldbackground="#f2f2f2")

        # ==============================
        #   BOTÕES SUPERIORES
        # ==============================
        frame_botoes = ctk.CTkFrame(self.janela)
        frame_botoes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Botão: Cadastro
        self.botao_Cadastrar = ctk.CTkButton(frame_botoes, text="Cadastrar aluno",
                                             command=self.cadastrar_aluno)
        self.botao_Cadastrar.pack(padx=5, pady=5, side=ctk.LEFT)

        # Botão: Busca por CPF
        self.botao_Buscar = ctk.CTkButton(frame_botoes, text="Buscar aluno",
                                          command=self.buscar_cpf)
        self.botao_Buscar.pack(padx=5, pady=5, side=ctk.LEFT)

        # Botão: Atualizar
        self.botao_Atualizar = ctk.CTkButton(frame_botoes, text="Atualizar aluno",
                                             command=self.atualizar_aluno)
        self.botao_Atualizar.pack(padx=5, pady=5, side=ctk.LEFT)

        # Botão: Excluir
        self.botao_Deletar = ctk.CTkButton(frame_botoes, text="Deletar aluno",
                                           command=self.deletar_aluno)
        self.botao_Deletar.pack(padx=5, pady=5, side=ctk.LEFT)

        # Botão: Listar
        self.botao_Listar = ctk.CTkButton(frame_botoes, text="Listar alunos",
                                          command=self.listar_todos)
        self.botao_Listar.pack(padx=5, pady=5, side=ctk.LEFT)

        # ==============================
        #   TREEVIEW PARA MOSTRAR ALUNOS
        # ==============================
        self.tree = ttk.Treeview(
            janela,
            columns=('ID', 'Nome', 'CPF', 'Telefone', 'data_matricula', 'Vencimento'),
            show="headings"
        )

        # Configura título e largura das colunas
        for coluna in self.tree["columns"]:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=5, padx=10)

        # Carrega lista inicial
        self.listar_todos()

    # ==============================
    #   MÁSCARA PARA DATAS
    # ==============================
    def aplicar_mascara_data(self, entry, event=None):
        # Obtém texto digitado
        text = entry.get()

        # Mantém apenas números
        text = ''.join([caractere for caractere in text if caractere.isdigit()])

        # Limita a 8 dígitos (DDMMAAAA)
        text = text[:8]

        # Constrói formato DD/MM/AAAA
        novo = ""
        if len(text) >= 1:
            novo += text[:2]  
        if len(text) >= 3:
            novo += "/" + text[2:4]
        if len(text) >= 5:
            novo += "/" + text[4:]

        # Atualiza campo
        entry.delete(0, "end")
        entry.insert(0, novo)

    # ==============================
    #   JANELA DE CADASTRO
    # ==============================
    def cadastrar_aluno(self):
        window = ctk.CTkToplevel(self.janela)
        window.geometry("550x450")
        window.grab_set()  # Impede interação com a janela principal
        window.title("Cadastrar aluno")

        # Campos de formulário
        self.label_nome = ctk.CTkLabel(window, text="Nome")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(window)
        self.entry_nome.pack(pady=5)

        self.label_cpf = ctk.CTkLabel(window, text="CPF")
        self.label_cpf.pack(pady=5)
        self.entry_cpf = ctk.CTkEntry(window)
        self.entry_cpf.pack(pady=5)

        self.label_telefone = ctk.CTkLabel(window, text="Telefone")
        self.label_telefone.pack(pady=5)
        self.entry_telefone = ctk.CTkEntry(window)
        self.entry_telefone.pack(pady=5)

        self.label_DatMatri = ctk.CTkLabel(window, text="Data Matricula")
        self.label_DatMatri.pack(pady=5)
        self.entry_DatMatri = ctk.CTkEntry(window)
        self.entry_DatMatri.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.entry_DatMatri, event))
        self.entry_DatMatri.pack(pady=5)

        self.label_Vencimento = ctk.CTkLabel(window, text="Vencimento")
        self.label_Vencimento.pack(pady=5)
        self.entry_Vencimento = ctk.CTkEntry(window)
        self.entry_Vencimento.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.entry_Vencimento, event))
        self.entry_Vencimento.pack(pady=5)

        # Função de salvar cadastro
        def salvar_cadastrar():
            nome = self.entry_nome.get()
            cpf = self.entry_cpf.get()
            telefone = self.entry_telefone.get()
            datmatri = self.entry_DatMatri.get()
            vencimento = self.entry_Vencimento.get()

            # Validação básica
            if not nome or not cpf:
                messagebox.showerror("Erro!", "Nome e CPF são obrigatórios")
                return
            
            try:
                aluno = Aluno(nome, cpf, telefone, datmatri, vencimento)
                self.db.cadastrar_aluno(aluno)
                messagebox.showinfo("Registrado!", "Aluno registrado com sucesso!")
                self.listar_todos()
                window.destroy()
            except Exception as e:
                messagebox.showerror("Erro!", str(e))

        # Botão salvar
        self.botao_salvar = ctk.CTkButton(window, text="Cadastrar aluno", command=salvar_cadastrar)
        self.botao_salvar.pack(pady=5)

    # ==============================
    #   LISTAR TODOS OS ALUNOS
    # ==============================
    def listar_todos(self):
        # Remove tudo e insere novamente
        self.tree.delete(*self.tree.get_children())
        for aluno in self.db.listar_todos():
            self.tree.insert('', 'end', values=aluno)

    # ==============================
    #   BUSCAR POR CPF
    # ==============================
    def buscar_cpf(self):
        cpf = simpledialog.askstring("Buscar", "Digite o CPF:")
        if not cpf:
            return

        aluno = self.db.buscar_cpf(cpf)

        self.tree.delete(*self.tree.get_children())

        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado!")
            return

        self.tree.insert('', 'end', values=aluno)

    # ==============================
    #   ATUALIZAR ALUNO
    # ==============================
    def atualizar_aluno(self):
        cpf = simpledialog.askstring("Atualizar", "Digite o CPF do aluno:")
        aluno = self.db.buscar_cpf(cpf)

        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado!")
            return
        
        janela_edit = ctk.CTkToplevel(self.janela)
        janela_edit.geometry("500x400")
        janela_edit.grab_set()
        janela_edit.title("Atualizar aluno")

        # Campo nome
        self.label_nomeEdit = ctk.CTkLabel(janela_edit, text="Nome")
        self.label_nomeEdit.pack(pady=5)
        self.entry_nomeEdit = ctk.CTkEntry(janela_edit)
        self.entry_nomeEdit.insert(0, aluno[1])
        self.entry_nomeEdit.pack(pady=5)

        # Telefone
        self.label_telEdit = ctk.CTkLabel(janela_edit, text="Telefone")
        self.label_telEdit.pack(pady=5)
        self.entry_telEdit = ctk.CTkEntry(janela_edit)
        self.entry_telEdit.insert(0, aluno[3])
        self.entry_telEdit.pack(pady=5)

        # Data matricula
        self.label_datMatriEdit = ctk.CTkLabel(janela_edit, text="Data matrícula")
        self.label_datMatriEdit.pack(pady=5)
        self.entry_datMatriEdit = ctk.CTkEntry(janela_edit)
        self.entry_datMatriEdit.insert(0, aluno[4])
        self.entry_datMatriEdit.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.entry_datMatriEdit, event))
        self.entry_datMatriEdit.pack(pady=5)

        # Vencimento
        self.label_vencEdit = ctk.CTkLabel(janela_edit, text="Vencimento")
        self.label_vencEdit.pack(pady=5)
        self.entry_vencEdit = ctk.CTkEntry(janela_edit)
        self.entry_vencEdit.insert(0, aluno[5])
        self.entry_vencEdit.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.entry_vencEdit, event))
        self.entry_vencEdit.pack(pady=5)

        # Função salvar atualização
        def salvar():
            nome = self.entry_nomeEdit.get()
            telefone = self.entry_telEdit.get()
            dataMatricula = self.entry_datMatriEdit.get()
            vencimento = self.entry_vencEdit.get()

            try:
                self.db.atualizar_alunos(cpf, nome, telefone, dataMatricula, vencimento)
                messagebox.showinfo("Atualizado!", "Aluno atualizado com sucesso!")
                janela_edit.destroy()
                self.listar_todos()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        ctk.CTkButton(janela_edit, command=salvar, text="Salvar alterações").pack(pady=5)

    # ==============================
    #   DELETAR ALUNO
    # ==============================
    def deletar_aluno(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "O Aluno não foi selecionado")
            return
        
        item = self.tree.item(selecionado[0])
        valores = item["values"]
        cpf = valores[2]

        confirmar = messagebox.askyesno("Confirmação", "Deseja excluir esse aluno ?")

        if confirmar:
            self.db.deletar_aluno(cpf)
            messagebox.showinfo("Concluido", "Aluno deletado com sucesso!")
            self.listar_todos()