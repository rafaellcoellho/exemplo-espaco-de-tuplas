import tkinter
from tkinter import ttk


class JanelaMoverEntreAmbientes(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Movimentação")

        self.interface_janela: tkinter.Frame = tkinter.Frame(self)
        self.interface_janela.grid(row=0, column=0, padx=10, pady=10)

        self.frame_mover_para_outro_ambiente: tkinter.LabelFrame = tkinter.LabelFrame(
            self.interface_janela,
            text="Mover para",
        )
        self.seletor_ambiente_alvo: ttk.Combobox = ttk.Combobox(
            self.frame_mover_para_outro_ambiente,
            values=["Ambiente 1", "Ambiente 2", "Ambiente 3"],
            state="readonly",
            font=("Arial", 15),
        )
        self.seletor_ambiente_alvo.current(0)
        self.botao_mover: tkinter.Button = tkinter.Button(
            self.frame_mover_para_outro_ambiente,
            text="Mover",
            command=self._mover_para_ambiente,
        )
        self._configurar_interface_gerenciador_mensagens()

    def _configurar_interface_gerenciador_mensagens(self):
        self.frame_mover_para_outro_ambiente.grid(row=0, column=0)
        self.frame_mover_para_outro_ambiente.grid_columnconfigure(0, weight=2)
        self.frame_mover_para_outro_ambiente.grid_columnconfigure(1, weight=1)

        self.seletor_ambiente_alvo.grid(row=0, column=0, sticky=tkinter.EW)
        self.botao_mover.grid(row=0, column=1, sticky=tkinter.EW)

    def _mover_para_ambiente(self):
        pass
