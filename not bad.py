import sys
import traceback
import os
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel
from PyQt5.QtGui import QPixmap
import math
import sqlite3

class MyWidget(QMainWindow):
    def dark(self):
        self.setStyleSheet("background-color:black;")
        self.pushButton.setStyleSheet("background-color: #272E39; color: #FFFFFF;")

    def __init__(self):
        super().__init__()
        uic.loadUi('star.ui', self)  # Загружаем дизайн
        self.pixmap = QPixmap('211.jpg')
        self.label.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.dark)
        self.pushButton_2.clicked.connect(self.stars)

    def mousePressEvent(self, event):
        global x
        global y
        x = int(round((event.x() / 100), 1) * 100)
        y = int(round((event.y() / 100), 1) * 100)

        conn = sqlite3.connect('starcoord.db')
        cursor = conn.cursor()

        cursor.execute('SELECT Name FROM coord WHERE x = ' + str(x) + ' AND y = ' + str(y))
        conn = sqlite3.connect('starinfo.db')
        self.results = cursor.fetchone()

        conn.close()
        if self.results:
            conn1 = sqlite3.connect('starinfo.db')
            cursor1 = conn1.cursor()


            self.q1 = cursor1.execute('SELECT constellation FROM starinfo WHERE Name = "' + str(self.results[0]) + '"')
            print('SELECT constellation FROM starinfo WHERE Name = "' + str(self.results[0]) + '"')
            self.results1 = cursor1.fetchall()

            self.q2 = cursor1.execute('SELECT type FROM starinfo WHERE Name = "' + str(self.results[0]) + '"')
            self.results2 = cursor1.fetchall()

            self.q3 = cursor1.execute('SELECT earth FROM starinfo WHERE Name = "' + str(self.results[0]) + '"')
            self.results3 = cursor1.fetchall()

            self.q4 = cursor1.execute('SELECT info FROM starinfo WHERE Name = "' + str(self.results[0]) + '"')
            self.results4 = cursor1.fetchall()
            conn1.close()

            self.a = Window2(self.results, self.results1, self.results2, self.results3, self.results4)
            self.a.show()

    def stars(self):
        print(x, y)
        x1 = x
        y1 = y
        self.label_122 = QLabel(self)
        self.label_122.move(x1 - 5, y1 - 5)
        self.label_122.resize(15, 15)
        self.pixmap1 = QPixmap('starr.png')
        self.label_122.setPixmap(self.pixmap1)
        self.label_122.show()




class Window2(QMainWindow):
        def dark(self):

             self.setStyleSheet("background-color:black;")
             self.pushButton.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.textEdit.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.textEdit_2.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.textEdit_3.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.textEdit_4.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.textEdit_5.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.pushButton_2.setStyleSheet("background-color: #272E39; color: #FFFFFF;")
             self.pushButton_3.setStyleSheet("background-color: #000000; color: #FFFFFF;")


        def ret(self):
            self.pushButton_3.setVisible(True)
            self.textEdit_5.setReadOnly(False)



        def __init__(self, arg, arg1, arg2, arg3, arg4):
            super(Window2, self).__init__()
            self.setWindowTitle('Window2')
            uic.loadUi('star2.ui', self)
            self.pushButton.clicked.connect(self.dark)
            self.pushButton_2.clicked.connect(self.ret)

            self.pushButton_3.setVisible(False)
            self.results = arg
            self.results1 = arg1
            self.results2 = arg2
            self.results3 = arg3
            self.results4 = arg4
            self.textEdit.setReadOnly(True)
            self.textEdit_2.setReadOnly(True)
            self.textEdit_3.setReadOnly(True)
            self.textEdit_4.setReadOnly(True)
            self.textEdit_5.setReadOnly(True)
            print(self.results1)

            if flag:

                self.pixmap = QPixmap(str(self.results1[0][0]).lower() + '.jpg')
                self.label.setPixmap(self.pixmap)
            self.textEdit.setText(str(self.results[0]))

            self.textEdit_2.setText(str(self.results1[0][0]))

            self.textEdit_3.setText(str(self.results2[0][0]))
            self.textEdit_4.setText(str(self.results3[0][0]))
            self.textEdit_5.setText(str(self.results4[0][0]))
            self.pushButton_3.clicked.connect(self.save)

        def save(self):
            conn2 = sqlite3.connect('starinfo.db')
            cursor2 = conn2.cursor()
            print(self.textEdit_5.toPlainText())
            print('UPDATE starinfo SET info = "' + str(self.textEdit_5.toPlainText()) + '" WHERE Name = "' + str(self.results[0]) + '"')
            cursor2.execute('UPDATE starinfo SET info = "' + str(self.textEdit_5.toPlainText()) + '" WHERE Name = "' + str(self.results[0]) + '"')
            conn2.commit()
            conn2.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
