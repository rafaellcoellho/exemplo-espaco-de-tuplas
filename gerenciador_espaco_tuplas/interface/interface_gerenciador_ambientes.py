import tkinter
from tkinter import messagebox


class InterfaceGerenciadorAmbientes(tkinter.LabelFrame):
    def __init__(self, frame_pai: tkinter.Frame):
        super().__init__(frame_pai, text="Gerenciador de Ambientes")

        self.frame_gerenciador_ambientes: tkinter.Frame = tkinter.Frame(self)
        self.frame_gerenciador_ambientes.grid(row=0, column=0, padx=10, pady=10)

        self.frame_adicionar_ambiente: tkinter.Frame = tkinter.Frame(
            self.frame_gerenciador_ambientes
        )
        self.label_nome_ambiente: tkinter.Label = tkinter.Label(
            self.frame_adicionar_ambiente, text="Novo:"
        )
        self.entrada_nome_novo_ambiente: tkinter.Entry = tkinter.Entry(
            self.frame_adicionar_ambiente
        )
        self.botao_adicionar_novo_ambiente: tkinter.Button = tkinter.Button(
            self.frame_adicionar_ambiente,
            text="Adicionar",
            command=self._adicionar_ambiente,
        )
        self._configurar_interface_adicionar_novo_ambiente()

    def _configurar_interface_adicionar_novo_ambiente(self):
        self.frame_adicionar_ambiente.grid(row=0, column=0)
        self.label_nome_ambiente.grid(row=0, column=0)
        self.entrada_nome_novo_ambiente.grid(row=0, column=1)
        self.botao_adicionar_novo_ambiente.grid(row=0, column=2)

    def _adicionar_ambiente(self):
        nome_novo_ambiente: str = self.entrada_nome_novo_ambiente.get()

        if nome_novo_ambiente == "":
            messagebox.showerror("Erro", "O nome do ambiente não pode ser vazio.")
            return

        self.entrada_nome_novo_ambiente.delete(0, tkinter.END)
        print(nome_novo_ambiente)
