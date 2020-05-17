from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from view_models.reservations_vm import ReservationsTableModel
from services.reservation_service import Reservation_service


class ReservationsWindow(QMdiSubWindow):
    object = None
    
    def __init__(self, mdi):
        if not ReservationsWindow.object:
            super().__init__()
            ReservationsWindow.object = self
            self.setAttribute(Qt.WA_DeleteOnClose, True)
            self.Render(mdi)
        self = ReservationsWindow.object

        self.showMaximized()

    def closeEvent(self, event):
        ReservationsWindow.object = None

    def Render(self, mdi):
        self.table = self.RenderApartmentsTable()
        self.setWidget(self.table)
        
        self.setWindowTitle("Reservations")
        mdi.addSubWindow(self)

    def RenderApartmentsTable(self):
        table = QTableView(self)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
      
        reservations = Reservation_service()
        self.reservation_data = reservations.reservation_list()
        self.model = ReservationsTableModel(self.reservation_data)
        table.setModel(self.model)

        return table