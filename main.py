from PyQt6.QtWidgets import QApplication


from modelo import Modelo
from vista import Vista
from controlador import Controlador


if __name__ == "__main__":
    app = QApplication([])
    windows = Vista("")
    modelo = Modelo()
    controlador = Controlador(modelo, windows)

    windows.show()
    app.exec()