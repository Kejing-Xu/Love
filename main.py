import os
from PyQt5 import QtWidgets
import sys
from start import Ui_start


class main_interaction(QtWidgets.QMainWindow, Ui_start):
    def __init__(self):
        super(main_interaction, self).__init__()
        self.setupUi(self)

    def click_start(self):
        os.system("python question_click.py")


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = main_interaction()
window.show()
sys.exit(app.exec_())
