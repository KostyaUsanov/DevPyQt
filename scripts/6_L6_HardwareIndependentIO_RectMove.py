from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.rect = QtCore.QRect(10, 10, 200, 100)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setStyle(QtCore.Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawRect(self.rect)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        x, y = event.pos().x(), event.pos().y()
        self.rect = QtCore.QRect(x, y, 200, 100)
        self.repaint()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        x, y = event.pos().x(), event.pos().y()
        self.rect = QtCore.QRect(x, y, 200, 100)
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = MyWidget()
    w.show()

    app.exec_()





