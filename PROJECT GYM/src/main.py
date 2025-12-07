import customtkinter as ctk
from interface import interfaceAcademia

def main():
    janela = ctk.CTk()
    app = interfaceAcademia(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()