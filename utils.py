from datetime import datetime


def get_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d,%H:%M:%S")


def check_value_in_lists(data_list, target_value):
    return any(inner_list and inner_list[0] == target_value for inner_list in data_list)
