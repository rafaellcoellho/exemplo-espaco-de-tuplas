import tkinter


class GerenciadorEspacoTuplas:
    def __init__(self):
        self.motor_interface_grafica: tkinter.Tk = tkinter.Tk()
        self._configurar_janela()

    def _configurar_janela(self):
        self.motor_interface_grafica.title("Gerenciador de Espaço de Tuplas")
        self.motor_interface_grafica.resizable(False, False)

    def iniciar(self):
        self.motor_interface_grafica.mainloop()


if __name__ == "__main__":
    gerenciador_espaco_tuplas: GerenciadorEspacoTuplas = GerenciadorEspacoTuplas()
    gerenciador_espaco_tuplas.iniciar()
