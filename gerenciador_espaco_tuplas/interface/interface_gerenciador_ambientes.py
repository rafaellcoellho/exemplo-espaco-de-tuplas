import tkinter
from tkinter import messagebox

from gerenciador_espaco_tuplas.interface.interface_janela_ambientes import (
    InterfaceJanelaAmbientes,
)


class InterfaceGerenciadorAmbientes(tkinter.LabelFrame):
    def __init__(self, frame_pai: tkinter.Frame):
        super().__init__(frame_pai, text="Gerenciador de Ambientes")

        self.frame_gerenciador_ambientes: tkinter.Frame = tkinter.Frame(self)
        self.frame_gerenciador_ambientes.grid(row=0, column=0, padx=10, pady=10)

        self.frame_adicionar_ambiente: tkinter.Frame = tkinter.Frame(
            self.frame_gerenciador_ambientes
        )
        self.entrada_nome_novo_ambiente: tkinter.Entry = tkinter.Entry(
            self.frame_adicionar_ambiente,
            font=("Arial", 15),
        )
        self.botao_adicionar_novo_ambiente: tkinter.Button = tkinter.Button(
            self.frame_adicionar_ambiente,
            text="Adicionar",
            command=self._adicionar_ambiente,
        )
        self._configurar_interface_adicionar_novo_ambiente()

        self.frame_mostrador_de_ambientes: tkinter.Frame = tkinter.Frame(
            self.frame_gerenciador_ambientes,
        )
        self.mostrador_de_ambientes: tkinter.Listbox = tkinter.Listbox(
            self.frame_mostrador_de_ambientes,
        )
        self.botao_ver_ambiente_selecionado: tkinter.Button = tkinter.Button(
            self.frame_mostrador_de_ambientes,
            text="Ver",
            command=self._ver_ambiente_selecionado,
        )
        self.botao_excluir_ambiente_selecionado: tkinter.Button = tkinter.Button(
            self.frame_mostrador_de_ambientes,
            text="Excluir",
            command=self._excluir_ambiente_selecionado,
        )
        self._configurar_interface_mostrador_de_ambientes()

    def _configurar_interface_adicionar_novo_ambiente(self):
        self.frame_adicionar_ambiente.grid(row=0, column=0)
        self.frame_adicionar_ambiente.grid_columnconfigure(0, weight=1)

        self.entrada_nome_novo_ambiente.grid(row=0, column=0)
        self.botao_adicionar_novo_ambiente.grid(row=0, column=1)

    def _configurar_interface_mostrador_de_ambientes(self):
        self.frame_mostrador_de_ambientes.grid(row=1, column=0, sticky=tkinter.EW)
        self.frame_mostrador_de_ambientes.grid_rowconfigure(0, weight=1)
        self.frame_mostrador_de_ambientes.grid_columnconfigure(0, weight=1)
        self.frame_mostrador_de_ambientes.grid_columnconfigure(1, weight=1)

        self.mostrador_de_ambientes.grid(
            row=0, column=0, columnspan=2, sticky=tkinter.EW
        )
        self.botao_ver_ambiente_selecionado.grid(row=1, column=0, sticky=tkinter.EW)
        self.botao_excluir_ambiente_selecionado.grid(row=1, column=1, sticky=tkinter.EW)

    def _adicionar_ambiente(self):
        nome_novo_ambiente: str = self.entrada_nome_novo_ambiente.get()

        if nome_novo_ambiente == "":
            messagebox.showerror("Erro", "O nome do ambiente não pode ser vazio.")
            return

        self.entrada_nome_novo_ambiente.delete(0, tkinter.END)
        print(nome_novo_ambiente)

    def _ver_ambiente_selecionado(self):
        ambiente_selecionado: str = self.mostrador_de_ambientes.curselection()
        InterfaceJanelaAmbientes()
        print(ambiente_selecionado)

    def _excluir_ambiente_selecionado(self):
        ambiente_selecionado: str = self.mostrador_de_ambientes.curselection()
        print(ambiente_selecionado)
