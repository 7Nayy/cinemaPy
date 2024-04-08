# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from film_tab import FilmTab
from reservation_tab import ReservationTab
from cinema_salle_tab import CinemaSalleTab


class CinemaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Cinéma")
        self.setGeometry(100, 100, 800, 600)

        # Initialiser les onglets
        self.table_widget = QTabWidget()
        self.setCentralWidget(self.table_widget)

        # Ajouter les onglets
        self.table_widget.addTab(FilmTab(), "Films")
        self.table_widget.addTab(ReservationTab(), "Réservations")
        self.table_widget.addTab(CinemaSalleTab(), "Cinémas et Salles")


if __name__ == "__main__":
    app = QApplication([])
    main = CinemaApp()
    main.show()
    app.exec_()
