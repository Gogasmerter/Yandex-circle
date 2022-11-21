import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Linux(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)  # Загружаем дизайн
        self.initUI()
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        print(event)
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_circle(qp)
        # Завершаем рисование
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor('yellow'))
        width = randint(100, 500)
        x, y = randint(0, 550 - width), randint(0, 550 - width)

        qp.drawEllipse(x, y, width, width)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Linux()
    ex.show()
    sys.exit(app.exec_())
