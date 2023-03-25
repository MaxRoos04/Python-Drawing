import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QLinearGradient
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Gradient Example')

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        size = self.size()

        gradient = QLinearGradient(0, 0, size.width(), size.height())
        gradient.setColorAt(0.0, Qt.red)
        gradient.setColorAt(0.5, Qt.yellow)
        gradient.setColorAt(1.0, Qt.green)

        brush = QBrush(gradient)

        qp.setBrush(brush)
        qp.setPen(Qt.NoPen)

        for i in range(10):
            x = i * 35
            y = i * 20
            w = 100
            h = 50
            qp.drawRect(x, y, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())