from PySide2 import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QDoubleValidator
from view_models.guests_vm import GuestTableModel
from services.guest_service import Guest_service


class GuestsWindow(QMdiSubWindow):
    object = None
    rowIdx = -1

    def __init__(self, mdi):
        if not GuestsWindow.object:
            super().__init__()
            GuestsWindow.object = self
            self.setAttribute(Qt.WA_DeleteOnClose, True)
            self.Render(mdi)
        self = GuestsWindow.object

        self.showMaximized()

    def closeEvent(self, event):
        GuestsWindow.object = None

    def Render(self, mdi):
        widget = QWidget()
        hbox = QHBoxLayout()

        self.table = self.RenderGuestsTable()

        grid = QGridLayout()
        grid.setMargin(20)
        grid.rowMinimumHeight(40)
        name_label = QLabel("Name")
        self.name_field = QLineEdit()
        last_name_label = QLabel("Last name")
        self.last_name_field = QLineEdit()
        age_label = QLabel("Age")
        self.age_field = QLineEdit()
        self.age_field.setValidator(QDoubleValidator(16, 100, 0))
        card_label = QLabel("Has card")
        self.card_field = QLineEdit()

        grid.addWidget(name_label, 0, 0, 1, 0)
        grid.addWidget(self.name_field, 1, 0, 1, 0)

        grid.addWidget(last_name_label, 2, 0, 1, 0)
        grid.addWidget(self.last_name_field, 3, 0, 1, 0)

        grid.addWidget(age_label, 4, 0, 1, 0)
        grid.addWidget(self.age_field, 5, 0, 1, 0)

        grid.addWidget(card_label, 6, 0, 1, 0)
        grid.addWidget(self.card_field, 7, 0, 1, 0)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.RemoveRow)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.SaveRow)

        grid.addWidget(delete_btn, 8, 0)
        grid.addWidget(save_btn, 8, 1)

        new_btn = QPushButton("New")
        new_btn.clicked.connect(self.NewRow)
        grid.addWidget(new_btn, 9, 0)

        filler = QSpacerItem(150, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        grid.addItem(filler, 10, 0)

        hbox.addWidget(self.table)
        hbox.addLayout(grid)

        widget.setLayout(hbox)
        self.setWidget(widget)

        self.setWindowTitle("Guests")
        mdi.addSubWindow(self)

    def RenderGuestsTable(self):
        table = QTableView(self)
        table.setMaximumWidth(500)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.clicked.connect(self.RowSelected)

        guests = Guest_service()
        self.guest_data = guests.guest_list()
        print(self.guest_data)
        self.model = GuestTableModel(self.guest_data, guests)
        table.setModel(self.model)

        return table

    @Slot()
    def RowSelected(self, arg):
        self.rowIdx = arg.row()
        model = arg.model()

        row = model.getData(self.rowIdx)
        self.name_field.setText(row['name'])
        self.last_name_field.setText(row['last_name'])
        self.age_field.setText(str(row['age']))
        self.card_field.setText(row['is_card'])

    @Slot()
    def RemoveRow(self):
        if self.rowIdx < 0:
            return

        self.model.removeRow(self.rowIdx)

    @Slot()
    def SaveRow(self):
        data = {
            "name": self.name_field.text(),
            "last_name": self.last_name_field.text(),
            "age": self.age_field.text(),
            "is_card": self.card_field.text()
        }
        self.model.updateRow(self.rowIdx, data)

    @Slot()
    def NewRow(self):
        self.rowIdx = -1
        self.name_field.setText('')
        self.last_name_field.setText('')
        self.age_field.setText('')
        self.card_field.setText('')
