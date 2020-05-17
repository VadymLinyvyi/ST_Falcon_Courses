from PySide2 import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QDoubleValidator
from view_models.apartments_vm import ApartmentsTableModel
from services.apartment_service import Apartment_service


class ApartmentsWindow(QMdiSubWindow):
    object = None
    rowIdx = -1
    
    def __init__(self, mdi):
        if not ApartmentsWindow.object:
            super().__init__()
            ApartmentsWindow.object = self
            self.setAttribute(Qt.WA_DeleteOnClose, True)
            self.Render(mdi)
        self = ApartmentsWindow.object

        self.showMaximized()

    def closeEvent(self, event):
        ApartmentsWindow.object = None


    def Render(self, mdi):
        widget = QWidget()
        vbox = QHBoxLayout()

        self.table = self.RenderApartmentsTable()

        grid = QGridLayout()
        grid.setMargin(20)
        grid.rowMinimumHeight(40)
        name_label = QLabel("Name")
        self.name_field = QLineEdit()
        price_label = QLabel("Price")
        self.price_field = QLineEdit()
        self.price_field.setValidator(QDoubleValidator(0, 100, 2))
        description_label = QLabel("Description")
        self.description_field = QLineEdit()

        grid.addWidget(name_label, 0, 0, 1, 0)
        grid.addWidget(self.name_field, 1, 0, 1, 0)

        grid.addWidget(price_label, 2, 0, 1, 0)
        grid.addWidget(self.price_field, 3, 0, 1, 0)

        grid.addWidget(description_label, 4, 0, 1, 0)
        grid.addWidget(self.description_field, 5, 0, 1, 0)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.RemoveRow)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.SaveRow)

        grid.addWidget(delete_btn, 6, 0)
        grid.addWidget(save_btn, 6, 1)

        new_btn = QPushButton("New")
        new_btn.clicked.connect(self.NewRow)
        grid.addWidget(new_btn, 7, 0)

        filler = QSpacerItem(150, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        grid.addItem(filler, 8, 0)

        vbox.addWidget(self.table)
        vbox.addLayout(grid)

        widget.setLayout(vbox)
        self.setWidget(widget)
        
        self.setWindowTitle("Apartments")
        mdi.addSubWindow(self)

    def RenderApartmentsTable(self):
        table = QTableView(self) 
        table.setMaximumWidth(500)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.clicked.connect(self.RowSelected)

        apartments = Apartment_service()
        self.apartment_data = apartments.apartments_list()
        self.model = ApartmentsTableModel(self.apartment_data, apartments)
        table.setModel(self.model)

        return table

    @Slot()
    def RowSelected(self, arg):
        self.rowIdx = arg.row()
        model = arg.model()

        row = model.getData(self.rowIdx)
        self.name_field.setText(row['name'])
        self.price_field.setText(str(row['price']))
        self.description_field.setText(row['description'])

    @Slot()
    def RemoveRow(self):
        if self.rowIdx < 0:
            return
        
        self.model.removeRow(self.rowIdx)

    @Slot()
    def SaveRow(self):
        data = {
            "name": self.name_field.text(),
            "price": self.price_field.text(),
            "description": self.description_field.text()
        }
        self.model.updateRow(self.rowIdx, data)

    @Slot()
    def NewRow(self):
        self.rowIdx = -1
        self.name_field.setText('')
        self.price_field.setText('')
        self.description_field.setText('')
