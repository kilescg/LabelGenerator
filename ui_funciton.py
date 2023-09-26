import os
import threading
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import jlink
import log

mac_id_list = []
header = ["macID"]

def Flash_Event(ui):
    thr = threading.Thread(target=Flashing_ThreadCallback, args=[ui])
    thr.start()
    ui.flashStatusLabel.setText("Flash Status : <span style=\"color:yellow\">In Progress</span></p>")

def Flashing_ThreadCallback(ui):
    jlink.Power_On()
    result = jlink.JLink_Program_Flash(os.path.join("program_files", ui.programFileComboBox.currentText()))
    if result:
        ui.flashStatusLabel.setText("Flash Status : <span style=\"color:green\">Success</span></p>")
    else:
        ui.flashStatusLabel.setText("Flash Status : <span style=\"color:red\">Fail</span></p>")

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
    mac_id = jlink.MAC_ID_Check()
    is_mac_id_duplicated = mac_id in mac_id_list
    if (mac_id == '') | (is_mac_id_duplicated):
        return
    mac_id_list.append(mac_id)
    if len(mac_id_list) == 3:
        log.WriteCsv(mac_id_list)
        mac_id_list = []
    PopulateTableView(ui.devicesTableView, header, mac_id_list)

def ClearList_Event(ui):
    mac_id_list = []
    PopulateTableView(ui.devicesTableView, header, mac_id_list)
    
def PrintNow_Event(ui):
    # todo
    log.WriteCsv(mac_id_list)
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