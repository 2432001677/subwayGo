import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.setWindowTitle('Tooltips')
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        # btn = QPushButton('Button', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.setGeometry(0, 0, 59, 49)

        ok_bt = QPushButton("OK")
        cancel_bt = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(ok_bt)
        hbox.addWidget(cancel_bt)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        # self.center()
        # self.resize(300, 200)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message', "Are you  OK?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


class Examp2(QMainWindow):  # 状态栏
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("ready")
        exitAction = QAction('Exit', self)
        exitAction.setStatusTip("exit app")
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(exitAction)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("title")
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    # ex = Example()
    ex = Examp2()
    sys.exit(app.exec_())
