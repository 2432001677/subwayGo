import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.setGeometry(0, 0, 59, 49)

        self.center()
        self.resize(200, 200)
        # self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
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


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
