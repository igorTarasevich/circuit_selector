from PyQt5 import QtCore, QtWidgets

class Add_Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Add_Browser, self).__init__()
        self.setupUi(self)

    def setupUi(self, add_browser_window):
        add_browser_window.setObjectName("MainWindow")
        add_browser_window.resize(447, 104)
        self.centralwidget = QtWidgets.QWidget(add_browser_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_name.setObjectName("label_name")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(340, 60, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_choose = QtWidgets.QLabel(self.centralwidget)
        self.label_choose.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_choose.setObjectName("label_choose")
        self.pushButton_choose = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose.setGeometry(QtCore.QRect(340, 20, 75, 23))
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(110, 20, 61, 16))
        self.label_path.setObjectName("label_path")
        add_browser_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_browser_window)
        QtCore.QMetaObject.connectSlotsByName(add_browser_window)

    def retranslateUi(self, add_browser_window):
        _translate = QtCore.QCoreApplication.translate
        add_browser_window.setWindowTitle(_translate("MainWindow", "Add new browser"))
        self.label_name.setText(_translate("MainWindow", "Enter name"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.label_choose.setText(_translate("MainWindow", "\".exe\" path"))
        self.pushButton_choose.setText(_translate("MainWindow", "Choose"))
        self.label_path.setText(_translate("MainWindow", ""))