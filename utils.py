from datetime import datetime
from PyQt5.QtGui import QStandardItemModel, QStandardItem


def get_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d,%H:%M:%S")


def check_value_in_lists(data_list, target_value):
    return any(inner_list and inner_list[0] == target_value for inner_list in data_list)


def populate_table_view(tableView, columnHeaders, data):
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
