import sys
import pyautogui
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtGui import QPixmap
import math
import sqlite3

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('star.ui', self)  # Загружаем дизайн
        self.pixmap = QPixmap('211.jpg')
        self.label.setPixmap(self.pixmap)

        conn = sqlite3.connect('starinfo.db')

        cursor = conn.cursor()

        cursor.execute("SELECT Название FROM starinfo")

        results = cursor.fetchall()

        print(results)

        conn.close()

        # Обратите внимание: имя элемента такое же как в QTDesigner

    def mousePressEvent(self, event):
        print(f"Координаты: {event.x()}, {event.y()}")
        print(int(round((event.x() / 100), 1) * 100), (int(round((event.y() / 100), 1) * 100)))
        #if (event.x / 10)

        #self.a = Window2()

        #self.a.show()



class Window2(QMainWindow):
        def __init__(self):
            super(Window2, self).__init__()
            self.setWindowTitle('Window2')
            uic.loadUi('star2.ui', self)
            self.pixmap = QPixmap('малая медведица.jpg')
            self.label.setPixmap(self.pixmap)


        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())