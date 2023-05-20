import tkinter
from tkinter import ttk


class InterfaceJanelaMensagensDeUsuario(tkinter.Frame):
    def __init__(self, janela: tkinter.Toplevel):
        super().__init__(janela)
        self.grid(row=0, column=0, padx=10, pady=10)

        self.frame_gerenciador_mensagens: tkinter.LabelFrame = tkinter.LabelFrame(
            self,
            text="Mensagens",
        )
        self.visualizador_de_mensagens: tkinter.Text = tkinter.Text(
            self.frame_gerenciador_mensagens,
            state=tkinter.DISABLED,
        )
        self.seletor_usuario_para_enviar_mensagem: ttk.Combobox = ttk.Combobox(
            self.frame_gerenciador_mensagens,
            values=["Usuário 1", "Usuário 2"],
            state="readonly",
            font=("Arial", 15),
        )
        self.seletor_usuario_para_enviar_mensagem.current(0)
        self.conteudo_mensagem: tkinter.Entry = tkinter.Entry(
            self.frame_gerenciador_mensagens,
            font=("Arial", 15),
        )
        self.botao_enviar_mensagem: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_mensagens,
            text="Enviar",
            command=self._enviar_mensagem,
        )
        self._configurar_interface_gerenciador_mensagens()

    def _configurar_interface_gerenciador_mensagens(self):
        self.frame_gerenciador_mensagens.grid(row=0, column=0)
        self.frame_gerenciador_mensagens.grid_columnconfigure(0, weight=2)
        self.frame_gerenciador_mensagens.grid_columnconfigure(1, weight=3)
        self.frame_gerenciador_mensagens.grid_columnconfigure(2, weight=1)

        self.visualizador_de_mensagens.grid(
            row=0, column=0, columnspan=3, sticky=tkinter.EW
        )
        self.seletor_usuario_para_enviar_mensagem.grid(
            row=1, column=0, sticky=tkinter.EW
        )
        self.conteudo_mensagem.grid(row=1, column=1, sticky=tkinter.EW)
        self.botao_enviar_mensagem.grid(row=1, column=2, sticky=tkinter.EW)

    def _enviar_mensagem(self):
        pass
