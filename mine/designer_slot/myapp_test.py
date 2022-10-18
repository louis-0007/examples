import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

# class MyApp(QtWidgets.QDialog):
# class MainWindow(QtWidgets.QDialog):
# class MainWindow(QtWidgets.QMainWindow):
class MyApp(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        # self.ui = uic.loadUi("./file/myapp.ui", self) # 두번째 전달인자에 self를 넣어주어야 합니다.
        self.ui = uic.loadUi("myapp.ui", self) # 두번째 전달인자에 self를 넣어주어야 합니다.
        self.ui.show()
    def start(self):
        self.ui.label_status.setText("start")
    def stop(self):
        self.ui.label_status.setText("stop")

app = QtWidgets.QApplication(sys.argv)
me = MyApp()
# me = MainWindow()
sys.exit(app.exec())