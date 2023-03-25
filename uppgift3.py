import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Rectangle Example')

        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)  
        self.drawRectangles(qp)
        qp.end()  

    def drawRectangles(self, qp):
        qp.setPen(QColor(168, 34, 3))
        size = self.size()

        for i in range(100):
            x = random.randint(1, size.width() - 50)
            y = random.randint(1, size.height() - 50)
            w = random.randint(1, 50)
            h = random.randint(1, 50)
            qp.drawRect(x, y, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
