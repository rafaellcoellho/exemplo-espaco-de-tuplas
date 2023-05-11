import tkinter
from tkinter import messagebox


class InterfaceCriadorTuplas(tkinter.LabelFrame):
    def __init__(self, frame_pai: tkinter.Frame, nome_tipo_tupla: str):
        super().__init__(frame_pai, text=nome_tipo_tupla)
        self.label_nome_tupla: tkinter.Label = tkinter.Label(
            self, text=nome_tipo_tupla, width=15
        )
        self.entrada_valor_tupla: tkinter.Entry = tkinter.Entry(self)
        self.botao_adicionar_tupla: tkinter.Button = tkinter.Button(
            self, text="Adicionar", command=self._adicionar_tupla
        )
        self._configurar_interface()

    def _configurar_interface(self):
        self.label_nome_tupla.grid(row=0, column=0)
        self.entrada_valor_tupla.grid(row=0, column=1)
        self.botao_adicionar_tupla.grid(row=0, column=2)

    def _adicionar_tupla(self):
        entrada_valor_tupla: str = self.entrada_valor_tupla.get()
        if entrada_valor_tupla == "":
            messagebox.showerror("Erro", "O valor da tupla não pode ser vazio")
            return

        self.entrada_valor_tupla.delete(0, tkinter.END)
        print(entrada_valor_tupla)
