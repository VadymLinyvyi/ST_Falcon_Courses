from PySide2 import *
from PySide2.QtCore import SIGNAL
from PySide2 import QtCore


class ReservationsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.reservations_data = data
        self.columns = {
            "Apt Name": "name",
            "Name": "user_name",
            "Card": "is_card",
            "Check-in": "check_in",
            "Check-out": "check_out",
            "Price": "price"
        }

    def getData(self, idx):
        return self.reservations_data[idx]

    def rowCount(self, *args, **kwargs):
        return len(self.reservations_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            keys = list(self.columns.keys())
            return keys[section]

    def data(self, index, role):
        row = self.reservations_data[index.row()]
        keys = list(self.columns.values())
        column = keys[index.column()]
        try:
            if role == QtCore.Qt.DisplayRole:
                return str(row[column])
        except KeyError:
            return None