import tkinter

from gerenciador_espaco_tuplas.interface_grafica.janelas.chat import (
    JanelaDeChat,
)


class JanelaDeAmbiente(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Ambiente")

        self.interface_janela: tkinter.Frame = tkinter.Frame(self)
        self.interface_janela.grid(row=0, column=0, padx=10, pady=10)

        self.frame_gerenciador_usuarios: tkinter.LabelFrame = tkinter.LabelFrame(
            self.interface_janela,
            text="Usuários",
        )
        self.mostrador_de_usuarios: tkinter.Listbox = tkinter.Listbox(
            self.frame_gerenciador_usuarios,
        )
        self.botao_mensagens_do_usuario: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_usuarios,
            text="Mensagens",
            command=self._ver_mensagens_do_usuario,
        )
        self.botao_mover_usuario_para_ambiente: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_usuarios,
            text="Mover",
            command=self._mover_usuario_para_ambiente,
        )
        self.botao_excluir_usuario: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_usuarios,
            text="Excluir",
            command=self._excluir_usuario,
        )
        self._configurar_interface_gerenciador_usuarios()

        self.frame_gerenciador_dispositivos: tkinter.LabelFrame = tkinter.LabelFrame(
            self.interface_janela,
            text="Dispositivos",
        )
        self.mostrador_de_dispositivos: tkinter.Listbox = tkinter.Listbox(
            self.frame_gerenciador_dispositivos,
        )
        self.botao_mover_dispositivo_para_ambiente: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_dispositivos,
            text="Mover",
            command=self._mover_dispositivo_para_ambiente,
        )
        self.botao_excluir_dispositivo: tkinter.Button = tkinter.Button(
            self.frame_gerenciador_dispositivos,
            text="Excluir",
            command=self._excluir_dispositivo,
        )
        self._configurar_interface_gerenciador_dispositivos()

    def _configurar_interface_gerenciador_usuarios(self):
        self.frame_gerenciador_usuarios.grid(row=0, column=0)
        self.frame_gerenciador_usuarios.grid_columnconfigure(0, weight=1)
        self.frame_gerenciador_usuarios.grid_columnconfigure(1, weight=1)
        self.frame_gerenciador_usuarios.grid_columnconfigure(2, weight=1)

        self.mostrador_de_usuarios.grid(
            row=0, column=0, columnspan=3, sticky=tkinter.EW
        )
        self.botao_mover_usuario_para_ambiente.grid(row=1, column=0, sticky=tkinter.EW)
        self.botao_excluir_usuario.grid(row=1, column=1, sticky=tkinter.EW)
        self.botao_mensagens_do_usuario.grid(row=1, column=2, sticky=tkinter.EW)

    def _configurar_interface_gerenciador_dispositivos(self):
        self.frame_gerenciador_dispositivos.grid(row=0, column=1)
        self.frame_gerenciador_dispositivos.grid_columnconfigure(0, weight=1)
        self.frame_gerenciador_dispositivos.grid_columnconfigure(1, weight=1)

        self.mostrador_de_dispositivos.grid(
            row=0, column=0, columnspan=2, sticky=tkinter.EW
        )
        self.botao_mover_dispositivo_para_ambiente.grid(
            row=1, column=0, sticky=tkinter.EW
        )
        self.botao_excluir_dispositivo.grid(row=1, column=1, sticky=tkinter.EW)

    def _ver_mensagens_do_usuario(self):
        ambiente_selecionado: str = self.mostrador_de_usuarios.curselection()
        JanelaDeChat()
        print(ambiente_selecionado)

    def _mover_usuario_para_ambiente(self):
        pass

    def _excluir_usuario(self):
        pass

    def _mover_dispositivo_para_ambiente(self):
        pass

    def _excluir_dispositivo(self):
        pass
