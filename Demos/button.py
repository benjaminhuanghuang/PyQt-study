import imp


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    # title
    self.setWindowTitle('Calculator')
    
    # Layout
    self.setLayout(QVBoxLayout())

    # Add button
    btn1 = QPushButton('test')
    self.layout().addWidget(btn1);

    #
    self.show()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWin = MainWindow()
  sys.exit(app.exec_())