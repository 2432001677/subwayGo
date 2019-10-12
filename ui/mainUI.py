# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#
import os
import platform

from PyQt5 import QtCore, QtGui, QtWidgets

from controller.subway_control import SubwayControl
from model.subway_caches import SubwayCache


class Ui_MainWindow(object):
    def __init__(self):
        self.sub_control = SubwayControl()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 580)
        MainWindow.setWindowOpacity(0.93)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QtGui.QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QtGui.QPalette.Window, QtCore.Qt.white)
        MainWindow.setPalette(pe)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(420, 80, 420, 131))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.box_end_route = QtWidgets.QComboBox(self.frame)
        self.box_end_route.setGeometry(QtCore.QRect(0, 90, 121, 41))
        self.box_end_route.setObjectName("box_end_route")
        self.box_start_route = QtWidgets.QComboBox(self.frame)
        self.box_start_route.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.box_start_route.setObjectName("box_start_route")
        self.box_start_station = QtWidgets.QComboBox(self.frame)
        self.box_start_station.setGeometry(QtCore.QRect(130, 0, 151, 41))
        self.box_start_station.setObjectName("box_start_station")
        self.box_end_station = QtWidgets.QComboBox(self.frame)
        self.box_end_station.setGeometry(QtCore.QRect(130, 90, 151, 41))
        self.box_end_station.setMaxVisibleItems(10)
        self.box_end_station.setMaxCount(21474)
        self.box_end_station.setObjectName("box_end_station")
        self.bt_best_route = QtWidgets.QPushButton(self.frame)
        self.bt_best_route.setGeometry(QtCore.QRect(290, 45, 130, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        font.setPointSize(18)
        font.setBold(True)
        self.bt_best_route.setFont(font)
        self.bt_best_route.setObjectName("bt_best_route")
        self.box_subway = QtWidgets.QComboBox(self.centralwidget)
        self.box_subway.setGeometry(QtCore.QRect(640, 10, 110, 35))
        self.bt_best_route.clicked.connect(self.best_path)

        if len(self.sub_control.subway_dirs) > 0:
            self.box_subway.addItems(self.sub_control.subway_dirs)
            self.box_start_route.addItems(self.sub_control.routes_start.routes_name)
            self.box_end_route.addItems(self.sub_control.routes_end.routes_name)
            self.box_start_station.addItems(self.sub_control.stations_start)
            self.box_end_station.addItems(self.sub_control.stations_end)
        self.box_subway.currentIndexChanged.connect(self.changed_system)
        self.box_start_route.currentIndexChanged.connect(lambda: self.changed_route(self.box_start_station, 0))
        self.box_end_route.currentIndexChanged.connect(lambda: self.changed_route(self.box_end_station, 1))

        self.box_subway.setObjectName("box_subway")
        self.label_subway = QtWidgets.QLabel(self.centralwidget)
        self.label_subway.setGeometry(QtCore.QRect(750, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_subway.setFont(font)
        self.label_subway.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_subway.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_subway.setObjectName("label_subway")
        self.label_start_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_start_pos.setGeometry(QtCore.QRect(320, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_start_pos.setFont(font)
        self.label_start_pos.setObjectName("label_start_pos")
        self.label_end_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_end_pos.setGeometry(QtCore.QRect(310, 170, 101, 51))
        self.label_end_pos.setFont(font)
        self.label_end_pos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_end_pos.setObjectName("label_end_pos")
        self.bt_swap = QtWidgets.QToolButton(self.centralwidget)
        self.bt_swap.setGeometry(QtCore.QRect(340, 120, 41, 51))
        self.bt_swap.clicked.connect(self.swap_station)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/swap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_swap.setIcon(icon)
        self.bt_swap.setIconSize(QtCore.QSize(50, 50))
        self.bt_swap.setObjectName("bt_swap")
        self.listView = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.listView.setFont(font)
        self.listView.setGeometry(QtCore.QRect(300, 250, 570, 281))
        self.listView.setObjectName("listView")

        self.box_routes = QtWidgets.QComboBox(self.centralwidget)
        self.box_routes.setGeometry(QtCore.QRect(25, 20, 130, 41))
        self.box_routes.setObjectName("box_best_routes")
        if len(self.sub_control.subway_dirs) > 0:
            self.box_routes.addItems(self.sub_control.routes_start.routes_name)
        self.bt_whole_route = QtWidgets.QPushButton(self.centralwidget)
        self.bt_whole_route.setGeometry(QtCore.QRect(160, 20, 110, 41))
        self.bt_whole_route.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bt_whole_route.setObjectName("bt_whole_route")
        self.bt_whole_route.clicked.connect(self.search_whole_route)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tableView.setFont(font)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 255, 450))
        self.tableView.setObjectName("tableView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.load_subway = QtWidgets.QAction(MainWindow)
        self.load_subway.setObjectName("load_subway")
        self.load_subway.triggered.connect(self.load_file)
        self.delete_subway = QtWidgets.QAction(MainWindow)
        self.delete_subway.setObjectName("delete_subway")
        self.delete_subway.triggered.connect(self.delete_system)
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.triggered.connect(QtWidgets.qApp.quit)
        self.menu.addAction(self.load_subway)
        self.menu.addAction(self.delete_subway)
        self.menu.addAction(self.quitAction)
        self.menubar.addAction(self.menu.menuAction())

        self.box_subway.setStyleSheet('''QComboBox{background:#42A5F5;font-size:25px;}''')
        self.label_subway.setStyleSheet('''QLabel{font-size:27px;font-family:Roman times;}''')
        self.bt_whole_route.setStyleSheet(
            '''QPushButton{color:white;font-size:20px;background:#6DDF6D;border-radius:15px;}''')

        self.bt_best_route.setStyleSheet('''QPushButton{color:white;background:#8CAECF;border-radius:10px;}''')
        self.label_start_pos.setStyleSheet('''QLabel{color:#7988CF;font-size:20px;font-family:Roman times;}''')
        self.label_end_pos.setStyleSheet('''QLabel{color:#7988CF;font-size:20px;font-family:Roman times;}''')
        self.bt_swap.setStyleSheet('''QPushButton{border-radius:15px;}''')
        if platform.system() == "Windows":
            self.box_start_route.setStyleSheet('''QComboBox{color:white;background:#8CAECF;border-radius:12px;}''')
            self.box_end_route.setStyleSheet('''QComboBox{color:white;background:#8CAECF;border-radius:12px;}''')
            self.box_start_station.setStyleSheet('''QComboBox{color:white;background:#8CAECF;border-radius:15px;}''')
            self.box_end_station.setStyleSheet('''QComboBox{color:white;background:#8CAECF;border-radius:15px;}''')
            self.box_routes.setStyleSheet(
                '''QComboBox{color:white;font-size:20px;background:#6DDF6D;border-radius:10px;}''')
        else:
            self.box_start_route.setStyleSheet('''QComboBox{background:#8CAECF;border-radius:12px;}''')
            self.box_end_route.setStyleSheet('''QComboBox{background:#8CAECF;border-radius:12px;}''')
            self.box_start_station.setStyleSheet('''QComboBox{background:#8CAECF;border-radius:15px;}''')
            self.box_end_station.setStyleSheet('''QComboBox{background:#8CAECF;border-radius:15px;}''')
            self.box_routes.setStyleSheet('''QComboBox{font-size:20px;background:#6DDF6D;border-radius:10px;}''')
        self.tableView.setStyleSheet('''QTableView{background:#B5DFB7;}''')
        self.listView.setStyleSheet('''QListView{color:darkblue;background:#8CAECF;}''')

        self.retranslateUi(MainWindow)
        self.bt_swap.clicked.connect(self.frame.repaint)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.box_subway, self.box_start_route)
        MainWindow.setTabOrder(self.box_start_route, self.box_start_station)
        MainWindow.setTabOrder(self.box_start_station, self.box_end_route)
        MainWindow.setTabOrder(self.box_end_route, self.box_end_station)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SubwayGo"))
        self.bt_best_route.setText(_translate("MainWindow", "查询路线"))
        self.label_subway.setText(_translate("MainWindow", "地铁系统"))
        self.label_start_pos.setText(_translate("MainWindow", "<html><head/><body><p>你的位置</p></body></html>"))
        self.label_end_pos.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">目的地</p></body></html>"))
        self.bt_whole_route.setText(_translate("MainWindow", "线路信息"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.load_subway.setText(_translate("MainWindow", "加载地铁系统"))
        self.delete_subway.setText(_translate("MainWindow", "删除当前系统"))
        self.quitAction.setText(_translate("MainWindow", "退出"))
        self.m_flag = False

    # 重写函数实现窗口拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def changed_system(self):  # 改变地铁系统
        self.box_start_route.clear()
        self.box_end_route.clear()
        self.box_start_station.clear()
        self.box_end_station.clear()
        self.box_routes.clear()
        self.sub_control.select_subway(self.box_subway.currentIndex())  # 通过读取下标选择地铁系统
        self.box_routes.addItems(self.sub_control.routes_start.routes_name)
        self.box_start_route.addItems(self.sub_control.routes_start.routes_name)  # 读取路线数据
        self.box_end_route.addItems(self.sub_control.routes_end.routes_name)
        self.box_start_station.addItems(self.sub_control.stations_start)  # 读取站点数据
        self.box_end_station.addItems(self.sub_control.stations_end)

    def changed_route(self, box, n):
        box.clear()
        if n == 0:
            self.sub_control.select_route_start(self.box_start_route.currentIndex())  # 通过读取下标选择线路
            box.addItems(self.sub_control.stations_start)  # 读取站点数据
        else:
            self.sub_control.select_route_end(self.box_end_route.currentIndex())
            box.addItems(self.sub_control.stations_end)

    def best_path(self):
        list_model = QtCore.QStringListModel()
        path = ["换乘路线信息及经过站点："]
        path.extend(
            self.sub_control.best_path(self.box_start_station.currentText(), self.box_end_station.currentText()))
        list_model.setStringList(path)
        self.listView.setModel(list_model)

    def swap_station(self):  # 交换起点和终点
        current_start_route = self.box_start_route.currentIndex()
        current_start_station = self.box_start_station.currentIndex()
        current_end_station = self.box_end_station.currentIndex()
        self.box_start_route.setCurrentIndex(self.box_end_route.currentIndex())
        self.box_end_route.setCurrentIndex(current_start_route)
        self.box_start_station.setCurrentIndex(current_end_station)
        self.box_end_station.setCurrentIndex(current_start_station)

    def search_whole_route(self):
        stations_name_status = self.sub_control.routes_start.get_stations_name_status(self.box_routes.currentIndex())
        self.whole_station_model = QtGui.QStandardItemModel(len(stations_name_status), 2)
        self.whole_station_model.setHorizontalHeaderLabels(["站点名", "是否开通"])
        self.whole_station_model.setVerticalHeaderLabels(
            self.sub_control.routes_start.get_pos(self.box_routes.currentIndex()))
        for j in range(len(stations_name_status)):
            self.whole_station_model.setItem(j, 0, QtGui.QStandardItem(stations_name_status[j][0]))
            self.whole_station_model.setItem(j, 1, QtGui.QStandardItem(stations_name_status[j][1]))
        self.tableView.setModel(self.whole_station_model)

    def load_file(self):
        self.box_subway.show()
        file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "\\",
                                                                    "Text Files (*.csv)")  # 设置文件扩展名过滤,用双分号间隔
        try:
            if file_name_choose != "":
                if platform.system() == "Windows":
                    file_name = file_name_choose.replace("/", "\\")
                    os.system("copy " + file_name + " " + os.getcwd() + "\\res")
                else:
                    os.system("cp " + file_name_choose + " " + os.getcwd() + "/res")
                file_name_choose = str(file_name_choose)
                file_name = file_name_choose.split('/')
                SubwayCache(file_name[len(file_name) - 1][:-4])
        except Exception as e:
            print(e, "csv文件格式错误")
        self.sub_control.search_system()
        self.box_subway.clear()
        self.box_subway.addItems(self.sub_control.subway_dirs)

    def delete_system(self):
        self.sub_control.delete_pk()
        self.sub_control.search_system()
        if len(self.sub_control.subway_dirs) > 0:
            self.box_subway.clear()
            self.box_subway.addItems(self.sub_control.subway_dirs)
            try:
                self.changed_system()
            except Exception as e:
                print(e)
        else:
            self.box_start_route.clear()
            self.box_end_route.clear()
            self.box_start_station.clear()
            self.box_end_station.clear()
            self.box_routes.clear()
            self.box_subway.close()
