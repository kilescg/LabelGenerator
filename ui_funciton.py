import os
import threading
import jlink
import log
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from utils import *

mac_id_list = []
header = ["macID"]


def Flash_Event(ui):
    thr = threading.Thread(target=Flashing_ThreadCallback, args=[ui])
    thr.start()
    ui.flashStatusLabel.setText(
        "Flash Status : <span style=\"color:yellow\">In Progress</span></p>")


def Flashing_ThreadCallback(ui):
    jlink.Power_On()
    result = jlink.JLink_Program_Flash(os.path.join(
        "program_files", ui.programFileComboBox.currentText()))
    if result:
        ui.flashStatusLabel.setText(
            "Flash Status : <span style=\"color:green\">Success</span></p>")
    else:
        ui.flashStatusLabel.setText(
            "Flash Status : <span style=\"color:red\">Fail</span></p>")


def ProgramFileComboBoxClick_Event(ui):
    program_files_folder = "program_files"

    # Clear the current items in the combobox
    currentText = ui.programFileComboBox.currentText()
    ui.programFileComboBox.clear()

    # Check if the folder exists
    if os.path.exists(program_files_folder) and os.path.isdir(program_files_folder):
        # Get a list of file names in the folder
        file_names = os.listdir(program_files_folder)

        # Filter out only the files (not directories) and add them to the combobox
        for file_name in file_names:
            file_path = os.path.join(program_files_folder, file_name)
            if os.path.isfile(file_path):
                ui.programFileComboBox.addItem(file_name)
                ui.programFileComboBox.setCurrentText(currentText)


def AddDevice_Event(ui):
    global mac_id_list
    global header
    jlink.Power_On()
    mac_id = [jlink.MAC_ID_Check()]
    global mac_id_test
    is_mac_id_duplicated = mac_id in mac_id_list
    if (mac_id == ['']):
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:red\">Cant read mac address</span></p>")
        return
    elif (is_mac_id_duplicated):
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:red\">mac address is duplicated</span></p>")
        return
    else:
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:green\">Okay</span></p>")
    mac_id_list.append(mac_id)
    log.LogMacID(mac_id[0], "database/devicesLog.csv")
    note = ui.noteLineEdit.text()
    data = (mac_id, 'good', note, '0', get_date_time())
    log.insert_device_incoming()
    if len(mac_id_list) == 3:
        log.WriteCsv(['macID'], mac_id_list, "database/devices.csv")
        for mac in mac_id_list:
            log.update_print_label_by_mac_id(mac)
        mac_id_list = []
    PopulateTableView(ui.devicesTableView, header, mac_id_list)


def ClearList_Event(ui):
    global mac_id_list
    mac_id_list = []
    PopulateTableView(ui.devicesTableView, header, mac_id_list)


def PrintNow_Event(ui):
    global mac_id_list
    # todo
    log.WriteCsv(['macID'], mac_id_list, "database/devices.csv")
    for mac in mac_id_list:
        log.update_print_label_by_mac_id(mac)
    mac_id_list = []
    PopulateTableView(ui.devicesTableView, header, mac_id_list)


def PopulateTableView(tableView, columnHeaders, data):
    # Create a model and set it for the table view
    model = QStandardItemModel()
    tableView.setModel(model)

    # Set column headers
    model.setHorizontalHeaderLabels(columnHeaders)

    # Populate the model with data
    for row in data:
        item_list = [QStandardItem(str(item)) for item in row]
        model.appendRow(item_list)

    tableView.resizeColumnsToContents()
