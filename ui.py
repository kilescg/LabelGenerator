# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConsoleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ConsoleGroupBox.setStyleSheet("    font-size: 12pt;\n"
"    font-family: Arial, sans-serif;")
        self.ConsoleGroupBox.setObjectName("ConsoleGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ConsoleGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.powerOptionButton = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.powerOptionButton.setObjectName("powerOptionButton")
        self.verticalLayout_5.addWidget(self.powerOptionButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.powerOnButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.powerOnButton.setObjectName("powerOnButton")
        self.horizontalLayout_2.addWidget(self.powerOnButton)
        self.powerOffButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.powerOffButton.setObjectName("powerOffButton")
        self.horizontalLayout_2.addWidget(self.powerOffButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.programFileLabel = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.programFileLabel.setObjectName("programFileLabel")
        self.horizontalLayout.addWidget(self.programFileLabel)
        self.flashStatusLabel = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.flashStatusLabel.setObjectName("flashStatusLabel")
        self.horizontalLayout.addWidget(self.flashStatusLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.programFileComboBox = QtWidgets.QComboBox(self.ConsoleGroupBox)
        self.programFileComboBox.setObjectName("programFileComboBox")
        self.verticalLayout_2.addWidget(self.programFileComboBox)
        self.flashButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.flashButton.setStyleSheet("")
        self.flashButton.setObjectName("flashButton")
        self.verticalLayout_2.addWidget(self.flashButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.devicesLabel = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.devicesLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.devicesLabel.setObjectName("devicesLabel")
        self.verticalLayout_5.addWidget(self.devicesLabel)
        self.devicesTableView = QtWidgets.QTableView(self.ConsoleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devicesTableView.sizePolicy().hasHeightForWidth())
        self.devicesTableView.setSizePolicy(sizePolicy)
        self.devicesTableView.setObjectName("devicesTableView")
        self.verticalLayout_5.addWidget(self.devicesTableView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statusLabel = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_3.addWidget(self.statusLabel, 0, QtCore.Qt.AlignHCenter)
        self.addDeviceStatusLabel = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.addDeviceStatusLabel.setText("")
        self.addDeviceStatusLabel.setObjectName("addDeviceStatusLabel")
        self.horizontalLayout_3.addWidget(self.addDeviceStatusLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.ConsoleGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.noteLineEdit = QtWidgets.QLineEdit(self.ConsoleGroupBox)
        self.noteLineEdit.setObjectName("noteLineEdit")
        self.verticalLayout_5.addWidget(self.noteLineEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addGoodDeviceButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.addGoodDeviceButton.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Darker Green */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #357a38; /* Even Darker Green when pressed */\n"
"}")
        self.addGoodDeviceButton.setObjectName("addGoodDeviceButton")
        self.horizontalLayout_5.addWidget(self.addGoodDeviceButton)
        self.addBadDeviceButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.addBadDeviceButton.setStyleSheet("QPushButton {\n"
"    background-color: #f44336; /* Red */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f; /* Darker Red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b71c1c; /* Even Darker Red when pressed */\n"
"}")
        self.addBadDeviceButton.setObjectName("addBadDeviceButton")
        self.horizontalLayout_5.addWidget(self.addBadDeviceButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.printNowButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.printNowButton.setStyleSheet("")
        self.printNowButton.setObjectName("printNowButton")
        self.horizontalLayout_4.addWidget(self.printNowButton)
        self.clearListButton = QtWidgets.QPushButton(self.ConsoleGroupBox)
        self.clearListButton.setStyleSheet("")
        self.clearListButton.setObjectName("clearListButton")
        self.horizontalLayout_4.addWidget(self.clearListButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.ConsoleGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConsoleGroupBox.setTitle(_translate("MainWindow", "Console"))
        self.powerOptionButton.setText(_translate("MainWindow", "J Link Power Option"))
        self.powerOnButton.setText(_translate("MainWindow", "Power on (Q)"))
        self.powerOffButton.setText(_translate("MainWindow", "Power Off (W)"))
        self.programFileLabel.setText(_translate("MainWindow", "Select your program"))
        self.flashStatusLabel.setText(_translate("MainWindow", "Flash Status : None"))
        self.flashButton.setText(_translate("MainWindow", "Flash Program (F)"))
        self.devicesLabel.setText(_translate("MainWindow", "Devices for Label Printing"))
        self.statusLabel.setText(_translate("MainWindow", "status :"))
        self.label.setText(_translate("MainWindow", "Note (Optional)"))
        self.addGoodDeviceButton.setText(_translate("MainWindow", "Add Good Devices (G)"))
        self.addBadDeviceButton.setText(_translate("MainWindow", "Add Faulty Devices (B)"))
        self.printNowButton.setText(_translate("MainWindow", "Print Now (P)"))
        self.clearListButton.setText(_translate("MainWindow", "Clear (C)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
