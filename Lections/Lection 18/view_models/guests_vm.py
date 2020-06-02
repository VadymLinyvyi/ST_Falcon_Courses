from PySide2 import *
from PySide2.QtCore import SIGNAL
from PySide2 import QtCore


class GuestTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, service):
        QtCore.QAbstractTableModel.__init__(self)
        self.guests_data = data
        print(data)
        self.columns = {
            "Name": "name",
            "Last name": "last_name",
            "Age": "age",
            "Has card": "is_card"
        }
        self.service = service

    def getData(self, idx):
        return self.guests_data[idx]

    def rowCount(self, *args, **kwargs):
        return len(self.guests_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            keys = list(self.columns.keys())
            return keys[section]

    def data(self, index, role):
        row = self.guests_data[index.row()]
        keys = list(self.columns.values())
        column = keys[index.column()]
        try:
            if role == QtCore.Qt.DisplayRole:
                return str(row[column])
        except KeyError:
            return None

    def updateRow(self, rowIdx, data):
        self.beginResetModel()
        self.service.update_data(data)
        self.guests_data = self.service.guest_list()
        self.endResetModel()
        return True

    def removeRow(self, row_id):
        self.beginResetModel()
        name = self.guests_data[row_id]['name']
        last_name = self.guests_data[row_id]['last_name']
        age = self.guests_data[row_id]['age']
        self.service.remove_guest(name, last_name, age)
        self.guests_data = self.service.guest_list()
        self.endResetModel()
        return True