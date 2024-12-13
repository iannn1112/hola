from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QTextEdit, QPushButton, QVBoxLayout, QLineEdit, QGridLayout

from PyQt6.QtGui import QFont


CALC_KEYBOARD = [
    ["(", ")", "CLEAR", "DEL"],
    ["1", "2", "3", "/"],
    ["4", "5", "6", "*"],
    ["7", "8", "9", "+"],
    [".", "0", "=", "-"],
]

#tipos de letras que me gustaron: Impact, Times New Roman.

DISPLAY_FONT = QFont("Times New Roman", 22)
KEYBOARD_FONT = QFont("Times New Roman", 16)

class Vista(QWidget):
    __display: QLineEdit
    __mapa__botones: dict[str, QPushButton] = {}

    def __init__(self, titulo, parent = None):
        QWidget.__init__(self, parent)
        QWidget.setWindowTitle(self, titulo)
        self.__crear_vista()

    def __crear_vista(self):

        self.__display = QLineEdit()
        self.__display.setReadOnly(True)
        self.__display.setFont(DISPLAY_FONT)
        self.__display.setMinimumHeight(50)

        contenedor_principal = QVBoxLayout()
        contenedor_teclado = QGridLayout()

        for i, row in enumerate(CALC_KEYBOARD):
            for j, key_data in enumerate(row):

                x, y, col_span, row_span, simbolo = i, j, 1, 1, key_data

                boton = QPushButton(simbolo)
                boton.setFont(KEYBOARD_FONT)
                boton.setMinimumSize(70, 70)

                self.__mapa__botones[simbolo] = boton

                contenedor_teclado.addWidget(boton, x, y, col_span, row_span)

        contenedor_principal.addWidget(self.__display)
        contenedor_principal.addLayout(contenedor_teclado)
        self.setLayout(contenedor_principal)

    @property
    def display(self) -> QLineEdit:
        return self.__display
    
    @property
    def mapa_botones(self) -> dict[str, QPushButton]:
        return self.__mapa__botones

        