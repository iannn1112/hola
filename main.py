from PyQt5.QtWidgets import QApplication


from modelo import Modelo
from vista import Vista
from controlador import Controlador



app = QApplication([])
windows = Vista("")
modelo = Modelo()
controlador = Controlador(modelo, windows)

windows.show()
app.exec_()