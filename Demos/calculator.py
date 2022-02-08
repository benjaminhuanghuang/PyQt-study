import imp


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QStyleFactory


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    # title
    self.setWindowTitle('Calculator')

    # create ui elements
    self.setLayout(QVBoxLayout())
    self.keypad()

    self.show()

  def keypad(self):
    container = QWidget()
    container.setLayout(QGridLayout())

    #
    result_field = QLineEdit()
    btn_result = QPushButton('Enter')
    btn_clear = QPushButton('Clear')
    btn_9 = QPushButton('9')
    btn_8 = QPushButton('8')
    btn_7 = QPushButton('7')
    btn_6 = QPushButton('6')
    btn_5 = QPushButton('5')
    btn_4 = QPushButton('4')
    btn_3 = QPushButton('3')
    btn_2 = QPushButton('2')
    btn_1 = QPushButton('1')
    btn_0 = QPushButton('0')
    btn_9 = QPushButton('Enter')
    btn_9 = QPushButton('Enter')
    btn_plus = QPushButton('+')
    btn_mins = QPushButton('-')
    btn_mult = QPushButton('*')
    btn_divd = QPushButton('/')
    # put into grid
    container.layout().addWidget(result_field, 0,0,1,4)
    container.layout().addWidget(btn_result, 1,0,1,2)
    container.layout().addWidget(btn_clear, 1,2,1,2)

    container.layout().addWidget(btn_9, 2,0)
    container.layout().addWidget(btn_8, 2,1)
    container.layout().addWidget(btn_7, 2,2)
    container.layout().addWidget(btn_plus, 2,3)

    container.layout().addWidget(btn_6, 3,0)
    container.layout().addWidget(btn_5, 3,1)
    container.layout().addWidget(btn_4, 3,2)
    container.layout().addWidget(btn_mins, 3,3)

    container.layout().addWidget(btn_3, 4,0)
    container.layout().addWidget(btn_2, 4,1)
    container.layout().addWidget(btn_1, 4,2)
    container.layout().addWidget(btn_mult, 4,3)

    container.layout().addWidget(btn_0, 5,0,1,3)
    container.layout().addWidget(btn_divd, 5,3)

    self.layout().addWidget(container)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWin = MainWindow()
  # apply style
  app.setStyle(QStyleFactory.create('Fusion')) 
  sys.exit(app.exec_())