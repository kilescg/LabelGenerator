from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
from ui_funciton import *
import sys
import os


def ConnectUiWithEvent(ui):
    ui.powerOnButton.clicked.connect(lambda: power_on_event())
    ui.powerOffButton.clicked.connect(lambda: power_off_event())
    ui.flashButton.clicked.connect(lambda: flash_event(ui))  # done

    ui.addGoodDeviceButton.clicked.connect(lambda: add_good_device_event(ui))
    ui.addBadDeviceButton.clicked.connect(lambda: add_bad_device_event(ui))
    ui.printNowButton.clicked.connect(lambda: print_now_event(ui))
    ui.clearListButton.clicked.connect(lambda: clear_list_event(ui))


def ComboBoxInitialize(ui):
    program_combobox_click_event(ui)


def SetTableHeader(ui):
    populate_table_view(ui.devicesTableView, header, [])


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Store the ui reference

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_G:
            add_good_device_event(self.ui)
        elif event.key() == Qt.Key_B:
            add_bad_device_event(self.ui)
        elif event.key() == Qt.Key_F:
            flash_event(self.ui)
        elif event.key() == Qt.Key_C:
            clear_list_event(self.ui)
        elif event.key() == Qt.Key_P:
            print_now_event(self.ui)
        elif event.key() == Qt.Key_Q:
            power_on_event(self.ui)
        elif event.key() == Qt.Key_W:
            power_off_event(self.ui)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = MyMainWindow(ui)
    ui.setupUi(MainWindow)
    ConnectUiWithEvent(ui)
    ComboBoxInitialize(ui)
    SetTableHeader(ui)
    MainWindow.show()
    sys.exit(app.exec_())
