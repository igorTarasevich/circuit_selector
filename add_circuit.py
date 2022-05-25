from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal


class Add_Circuit(QtWidgets.QMainWindow):
    # circuit_name = pyqtSignal(str)

    def __init__(self):
        super(Add_Circuit, self).__init__()
        self.setupUi(self)

    def setupUi(self, add_circuit_window):
        add_circuit_window.setObjectName("MainWindow")
        add_circuit_window.resize(357, 67)
        self.centralwidget = QtWidgets.QWidget(add_circuit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_name.setObjectName("label_name")
        self.pushButton_name = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_name.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.pushButton_name.setObjectName("pushButton_name")
        # self.pushButton_name.clicked.connect(self.send_data)
        add_circuit_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_circuit_window)
        QtCore.QMetaObject.connectSlotsByName(add_circuit_window)

    def retranslateUi(self, add_circuit_window):
        _translate = QtCore.QCoreApplication.translate
        add_circuit_window.setWindowTitle(_translate("MainWindow", "Add new circuit"))
        self.label_name.setText(_translate("MainWindow", "Enter name"))
        self.pushButton_name.setText(_translate("MainWindow", "Add"))

    # def send_data(self):
    #     self.circuit_name.emit(self.lineEdit_name.text())
    #     self.close()

