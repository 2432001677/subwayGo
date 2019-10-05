import sys
from controller import route_control,subway_control,station_control
from ui.mainUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sub_system=subway_control.SubwayControl()

    sys.exit(app.exec_())
