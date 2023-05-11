import tkinter

from gerenciador_espaco_tuplas.interface.interface_criador_tuplas import (
    InterfaceCriadorTuplas,
)


class GerenciadorEspacoTuplas:
    def __init__(self):
        self.motor_interface_grafica: tkinter.Tk = tkinter.Tk()
        self._configurar_janela()

        self.frame_gerenciador_espaco_tuplas: tkinter.Frame = tkinter.Frame(
            self.motor_interface_grafica
        )

        self.interface_criador_ambientes: InterfaceCriadorTuplas = (
            InterfaceCriadorTuplas(
                frame_pai=self.frame_gerenciador_espaco_tuplas,
                nome_tipo_tupla="ambiente",
            )
        )
        self.interface_criador_dispositivos: InterfaceCriadorTuplas = (
            InterfaceCriadorTuplas(
                frame_pai=self.frame_gerenciador_espaco_tuplas,
                nome_tipo_tupla="dispositivo",
            )
        )
        self.interface_criador_usuarios: InterfaceCriadorTuplas = (
            InterfaceCriadorTuplas(
                frame_pai=self.frame_gerenciador_espaco_tuplas,
                nome_tipo_tupla="usuário",
            )
        )
        self._configurar_interface()

    def _configurar_janela(self):
        self.motor_interface_grafica.title("Gerenciador de Espaço de Tuplas")
        self.motor_interface_grafica.resizable(False, False)

    def _configurar_interface(self):
        self.frame_gerenciador_espaco_tuplas.grid(row=0, column=0, padx=10, pady=10)
        self.interface_criador_ambientes.grid(row=0, column=1)
        self.interface_criador_dispositivos.grid(row=0, column=2)
        self.interface_criador_usuarios.grid(row=0, column=3)

    def iniciar(self):
        self.motor_interface_grafica.mainloop()


if __name__ == "__main__":
    gerenciador_espaco_tuplas: GerenciadorEspacoTuplas = GerenciadorEspacoTuplas()
    gerenciador_espaco_tuplas.iniciar()
