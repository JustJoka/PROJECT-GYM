# 🏋️ Sistema de Cadastro de Alunos — Academia
Aplicação desenvolvida em **Python + CustomTkinter** para gerenciamento de alunos de academia. 
Permite **cadastrar, listar, buscar, atualizar e deletar alunos**, com armazenamento em **SQLite**.

---

## 📌 Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| ➕ Cadastrar aluno | Adiciona um novo aluno com Nome, CPF, Telefone, Data de Matrícula e Vencimento. |
| 🔍 Buscar aluno | Pesquisa um aluno pelo CPF. |
| ✏ Atualizar aluno | Permite editar dados existentes. |
| 🗑 Deletar aluno | Remove um aluno do banco de dados. |
| 📋 Listar alunos | Exibe todos os alunos em um TreeView. |
| 🗂 Validação | Máscara automática para datas (DD/MM/AAAA). |

---

## 🛠 Tecnologias Utilizadas

- Python 3.x  
- CustomTkinter  
- Tkinter  
- SQLite3  

---

## 📂 Estrutura do Projeto

/projeto-academia<br>
│<br>
├── src/<br>
  ├── academia.db<br>
│ ├── main.py<br>
│ ├── interface.py<br>
│ ├── aluno.py<br>
│ └── banco.py<br>
│<br>
├── database/<br>
│ └── academia.db (gerado automaticamente)<br>
│<br>
├── README.md<br>
├── requirements.txt<br>
├── LICENSE<br>
└── .gitignore<br>
<br>
yaml
Copiar código

---

## ▶ Como Executar

### 1️⃣ Clone o repositório
bash
git clone https://github.com/seu-usuario/projeto-academia.git
cd projeto-academia
2️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
3️⃣ Execute o sistema
bash
Copiar código
python src/main.py
🧠 Sobre o Sistema
O sistema utiliza:

CustomTkinter para uma interface moderna e amigável

SQLite como banco de dados local

Padrão de projeto simples, com classes separadas:

Aluno → Representa um aluno

BancoDeDados → Faz CRUD no SQLite

interfaceAcademia → Controla toda a interface gráfica

main.py → Início da aplicação

📸 Capturas de Tela (opcional)
Você pode adicionar imagens do sistema em /assets:

bash
Copiar código
/assets
   ├── tela_principal.png
   ├── cadastro.png
   └── edicao.png
Depois adicionar no README:

markdown
Copiar código

![Preview](https://github.com/JustJoka/PROJECT-GYM/blob/main/PROJECT_GYM/assets/Screenshot%202025-12-07%20065831.png?raw=true)
![Preview](https://github.com/JustJoka/PROJECT-GYM/blob/main/PROJECT_GYM/assets/Screenshot%202025-12-07%20065554.png?raw=true)
![Preview](https://github.com/JustJoka/PROJECT-GYM/blob/main/PROJECT_GYM/assets/Screenshot%202025-12-07%20065427.png?raw=true)





