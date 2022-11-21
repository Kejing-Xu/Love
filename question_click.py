import os
from PyQt5 import QtWidgets
import sys
from question import Ui_question
import webbrowser


class Sign(QtWidgets.QMainWindow, Ui_question):
    def __init__(self):
        super(Sign, self).__init__()
        self.setupUi(self)

    def click_comfirm(self):
        get_date=self.lineEdit.text()
        if get_date =='20211217':
            url = "file:///E:/html/city%20of%20stars.html"
            webbrowser.open(url, new=2)
        else:
            os.system("python wrong.py")


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = Sign()
window.show()
sys.exit(app.exec_())