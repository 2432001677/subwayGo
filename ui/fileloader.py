# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileloader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 95)
        self.bt = QtWidgets.QDialogButtonBox(Dialog)
        self.bt.setGeometry(QtCore.QRect(300, 20, 81, 51))
        self.bt.setOrientation(QtCore.Qt.Vertical)
        self.bt.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bt.setObjectName("bt")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.bt_choose_file = QtWidgets.QPushButton(Dialog)
        self.bt_choose_file.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.bt_choose_file.setObjectName("bt_choose_file")

        self.retranslateUi(Dialog)
        # self.bt.accepted.connect(Dialog.accept)
        # self.bt.rejected.connect(Dialog.reject)
        self.bt.accepted.connect(self.ok)
        self.bt.rejected.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bt_choose_file.setText(_translate("Dialog", "选择文件"))

    def ok(self):
        QtWidgets.QDialog.close(self)
        return 1

    def cancel(self):
        QtWidgets.QDialog.close(self)
        return 0


class ChooseFile(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(ChooseFile,self).__init__(parent)
        self.setupUi(self)
