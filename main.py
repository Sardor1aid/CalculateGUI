from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import math
from PyQt5.QtCore import QTimer
from datetime import datetime

from py_windows.mainScreen import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Простая программа")
        self.label.setText("")
        self.numeric = ""

        self.pushButton_3.clicked.connect(self.add_label_zero)
        self.pushButton.clicked.connect(self.add_label_one)
        self.pushButton_4.clicked.connect(self.add_label_two)
        self.pushButton_6.clicked.connect(self.add_label_three)
        self.pushButton_7.clicked.connect(self.add_label_four)
        self.pushButton_8.clicked.connect(self.add_label_five)
        self.pushButton_5.clicked.connect(self.add_label_six)
        self.pushButton_10.clicked.connect(self.add_label_seven)
        self.pushButton_11.clicked.connect(self.add_label_eight)
        self.pushButton_12.clicked.connect(self.add_label_nine)
        self.pushButton_20.clicked.connect(self.add_label_plus)
        self.pushButton_19.clicked.connect(self.add_label_minus)
        self.pushButton_18.clicked.connect(self.add_label_multiply)
        self.pushButton_17.clicked.connect(self.add_label_divide)
        self.pushButton_15.clicked.connect(self.add_label_percent)
        self.pushButton_14.clicked.connect(self.add_label_exponentiation)
        self.pushButton_2.clicked.connect(self.add_label_del)
        self.pushButton_16.clicked.connect(self.add_label_sqrt)
        self.pushButton_13.clicked.connect(self.add_label_cos)
        self.pushButton_9.clicked.connect(self.add_label_equally)
        self.pushButton_21.clicked.connect(self.add_label_open)
        self.pushButton_22.clicked.connect(self.add_label_close)

        self.update_time()  # Первоначальное обновление времени
        self.timer = QTimer(self)  # Создание таймера
        self.timer.timeout.connect(self.update_time)  # Подключение функции обновления времени
        self.timer.start(1000)  # Установка интервала таймера в 1000 мс (1 секунда)

    def update_time(self):
        current_time = datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        time_str = time_str.split(" ")  # Получил список с двумя элементами -> [дата, время]
        self.label_2.setText(time_str[1])
        self.label_3.setText(time_str[0])
        
    def add_label_open(self):
        self.numeric += "("
        self.label.setText(self.numeric)

    def add_label_close(self):
        self.numeric += ")"
        self.label.setText(self.numeric)


    def add_label_zero(self):
        self.numeric += "0"
        self.label.setText(self.numeric)

    def add_label_one(self):
        self.numeric += "1"
        self.label.setText(self.numeric)

    def add_label_two(self):
        self.numeric += "2"
        self.label.setText(self.numeric)

    def add_label_three(self):
        self.numeric += "3"
        self.label.setText(self.numeric)
    
    def add_label_four(self):
        self.numeric += "4"
        self.label.setText(self.numeric)
    
    def add_label_five(self):
        self.numeric += "5"
        self.label.setText(self.numeric)

    def add_label_six(self):
        self.numeric += "6"
        self.label.setText(self.numeric)

    def add_label_seven(self):
        self.numeric += "7"
        self.label.setText(self.numeric)

    def add_label_eight(self):
        self.numeric += "8"
        self.label.setText(self.numeric)

    def add_label_nine(self):
        self.numeric += "9"
        self.label.setText(self.numeric)

    def add_label_plus(self):
        self.numeric += "+"
        self.label.setText(self.numeric)

    def add_label_minus(self):
        self.numeric += "-"
        self.label.setText(self.numeric)

    def add_label_multiply(self):
        self.numeric += "*"
        self.label.setText(self.numeric)

    def add_label_divide(self):
        self.numeric += ":"
        self.label.setText(self.numeric)

    def add_label_percent(self):
        self.numeric += "%"
        self.label.setText(self.numeric)
    
    def add_label_exponentiation(self):
        self.numeric += "**"
        self.label.setText(self.numeric)

    def add_label_del(self):
        self.numeric = self.numeric[:-1]
        self.label.setText(self.numeric)

    def add_label_sqrt(self):
        self.numeric += "√"
        self.label.setText(self.numeric)
    
    def add_label_cos(self):
        self.numeric += "cos"
        self.label.setText(self.numeric)

    def add_label_equally(self):
        result = ""


        if "√" in self.numeric:
            if isinstance(int(self.numeric[1:])**0.5, float):
                result = int(self.numeric[1:])** 0.5
                self.numeric = ""
                self.numeric += str(round(result, 4))
            else:
                result = int(self.numeric[1:]) ** 0.5
                self.numeric = ""
                self.numeric += str(result)


        elif "cos" in self.numeric:
            result = int(self.numeric[3:])
            self.numeric = ""
            self.numeric += str(round(math.cos(result),4))

        else:
            result += str(eval(self.numeric))
            self.label.setText(result)
            self.numeric = ""
            self.numeric += result
        


def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()


