from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QPushButton, QWidget
from film_tab import FilmTab
from reservation_tab import ReservationTab
from cinema_salle_tab import CinemaSalleTab
from seance_tab import SeanceTab

class CinemaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Cinéma")
        self.setGeometry(100, 100, 800, 600)

        # Initialiser les onglets
        self.table_widget = QTabWidget()
        self.setCentralWidget(self.table_widget)

        # Ajouter les onglets
        self.film_tab = FilmTab()
        self.reservation_tab = ReservationTab()
        self.cinema_salle_tab = CinemaSalleTab()
        self.seance_tab = SeanceTab()

        self.table_widget.addTab(self.film_tab, "Films")
        self.table_widget.addTab(self.reservation_tab, "Réservations")
        self.table_widget.addTab(self.cinema_salle_tab, "Cinémas et Salles")
        self.table_widget.addTab(self.seance_tab, "Séances")

        # Ajouter le bouton de mise à jour
        update_button = QPushButton("Mettre à jour l'application")
        update_button.clicked.connect(self.update_application)

        main_layout = QVBoxLayout()
        main_layout.addWidget(update_button)
        main_layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def update_application(self):
        self.film_tab.load_films()
        self.reservation_tab.load_reservations()
        self.cinema_salle_tab.update_cinemas_display()
        self.cinema_salle_tab.update_salles_display()
        self.seance_tab.update_seances_display()

if __name__ == "__main__":
    app = QApplication([])
    main = CinemaApp()
    main.show()
    app.exec_()
