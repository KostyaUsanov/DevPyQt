"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""

from PySide6 import QtWidgets

from newform_a import Ui_Form  # Импортируем класс формы


class Window(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonMirror.clicked.connect(self.mirror)
        self.ui.lineEditInput.textEdited.connect(self.mirror)
        self.ui.lineEditMirror.textChanged.connect(lambda x: self.ui.lineEdit_3.setText(x[::-1]))
        self.ui.radioButton.toggled.connect(self.radio)
    def mirror(self):
        input_text = self.ui.lineEditInput.text()[::-1]
        self.ui.lineEditMirror.setText(input_text)

    def radio(self, param):
        if param:
            self.ui.lineEdit_3.setText('Кнопка нажата')
        else:
            self.ui.lineEdit_3.setText('Кнопка отжата')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
