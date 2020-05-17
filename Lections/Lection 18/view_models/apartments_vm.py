from PySide2 import *
from PySide2.QtCore import SIGNAL
from PySide2 import QtCore


class ApartmentsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, service):
        QtCore.QAbstractTableModel.__init__(self)
        self.apartments_data = data
        self.columns = {
            "Name": "name", 
            "Price": "price", 
            "Description": "description", 
            "Smoke": "smoke_allowed"
        }
        self.service = service

    def getData(self, idx):
        return self.apartments_data[idx]

    def rowCount(self, *args, **kwargs):
        return len(self.apartments_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            keys = list(self.columns.keys())
            return keys[section]

    def data(self, index, role):
        row = self.apartments_data[index.row()]
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
        self.apartments_data = self.service.apartments_list()
        self.endResetModel()
        return True

    def removeRow(self, row_id):
        self.beginResetModel()
        name = self.apartments_data[row_id]['name']
        self.service.remove_apartment(name)
        self.apartments_data = self.service.apartments_list()
        self.endResetModel()
        return True