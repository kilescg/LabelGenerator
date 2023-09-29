from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
from ui_funciton import *
import sys


def ConnectUiWithEvent(ui):
    ui.flashButton.clicked.connect(lambda: Flash_Event(ui))  # done

    ui.addDeviceButton.clicked.connect(lambda: AddDevice_Event(ui))
    ui.printNowButton.clicked.connect(lambda: PrintNow_Event(ui))
    ui.clearListButton.clicked.connect(lambda: ClearList_Event(ui))


def ComboBoxInitialize(ui):
    ProgramFileComboBoxClick_Event(ui)


def SetTableHeader(ui):
    PopulateTableView(ui.devicesTableView, header, [])


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Store the ui reference

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            AddDevice_Event(self.ui)


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
