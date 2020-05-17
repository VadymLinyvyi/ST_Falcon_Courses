import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMdiArea, QMessageBox
from PySide2.QtCore import Slot

from views.add_reservation_window import AddReservationWindow
from views.apartments_window import ApartmentsWindow
from views.guests_window import GuestsWindow
from views.reservations_window import ReservationsWindow
from views.main_window import MainWindow
import services.mongo_setup as db_setup


class MDIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        menu = self.menuBar()

        apartments = menu.addAction("Apartments")
        apartments.triggered.connect(self.ShowApartments)

        reservations = menu.addMenu("Reservations")
        reservations_add = reservations.addAction("Add")
        reservations_add.setShortcut('Ctrl+N')
        reservations_add.triggered.connect(self.AddReservations)
        reservations_view = reservations.addAction("View")
        reservations_view.triggered.connect(self.ShowReservations)

        users = menu.addAction("Users")
        users.triggered.connect(self.ShowUsers)

        help = menu.addAction("Help")
        help.triggered.connect(self.ShowHelp)

        self.setWindowTitle("Hotel app")
        self.ShowMainWindow()

    @Slot()
    def ShowMainWindow(self):
        self.main_window = MainWindow(self.mdi)
        self.main_window.showMaximized()

    @Slot()
    def AddReservations(self):
        print("reservations add")
        self.closeMainWindow()
        add_reservations_window = AddReservationWindow(self.mdi)
        add_reservations_window.destroyed.connect(self.ShowMainWindow)
        add_reservations_window.createNewUser.connect(self.ShowUsers)

    @Slot()
    def ShowReservations(self):
        print("reservations view")
        self.closeMainWindow()
        reservations_window = ReservationsWindow(self.mdi)
        reservations_window.destroyed.connect(self.ShowMainWindow)

    @Slot()
    def ShowApartments(self, p):
        #add singleton
        self.closeMainWindow()
        apartments_window = ApartmentsWindow(self.mdi)
        apartments_window.destroyed.connect(self.ShowMainWindow)

    @Slot()
    def ShowUsers(self):
        #add singleton
        self.closeMainWindow()
        users_window = GuestsWindow(self.mdi)
        users_window.destroyed.connect(self.ShowMainWindow)

    @Slot()
    def ShowHelp(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is help")
        msg.exec_()
        print("Help")

    def closeMainWindow(self):
        if self.main_window:
            self.main_window.close()
            self.main_window = None


if __name__ == "__main__":
    db_setup.global_init()

    app = QApplication(sys.argv)
    mdi = MDIWindow()

    mdi.setMaximumSize(800, 600)
    mdi.setMinimumSize(800, 600)

    mdi.show()
    app.exec_()
