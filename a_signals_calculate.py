"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from calculate import Ui_calculate


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_calculate()
        self.ui.setupUi(self)

        self.ui.One.clicked.connect(lambda: self.calc(self.ui.One.text()))
        self.ui.Two.clicked.connect(lambda: self.calc(self.ui.Two.text()))
        self.ui.Three.clicked.connect(lambda: self.calc(self.ui.Three.text()))
        self.ui.Minus.clicked.connect(lambda: self.calc(self.ui.Minus.text()))
        self.ui.Plus.clicked.connect(lambda: self.calc(self.ui.Plus.text()))
        self.ui.Clear.clicked.connect(self.clear)

    def calc(self, number):
        self.ui.ShowResult.setText(self.ui.ShowResult.text() + number)

    def clear(self):
        self.ui.ShowResult.clear()

    def




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
