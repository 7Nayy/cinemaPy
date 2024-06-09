from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from database import fetch_all_reservations

class ReservationTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Formulaire de recherche de réservation
        self.form_layout = QFormLayout()
        self.reservation_number_input = QLineEdit()
        self.form_layout.addRow("Numéro de Réservation:", self.reservation_number_input)

        self.search_button = QPushButton("Rechercher")
        self.search_button.clicked.connect(self.search_reservation_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.search_button)

        # Table pour afficher les résultats de recherche
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Utilisateur", "Film", "Nombre de Places"])
        layout.addWidget(self.results_table)

        self.setLayout(layout)

    def load_reservations(self):
        self.results_table.setRowCount(0)  # Réinitialiser la table
        reservations = fetch_all_reservations()
        for reservation in reservations:
            row_position = self.results_table.rowCount()
            self.results_table.insertRow(row_position)
            self.results_table.setItem(row_position, 0, QTableWidgetItem(reservation['Utilisateur']))
            self.results_table.setItem(row_position, 1, QTableWidgetItem(reservation['Film']))
            self.results_table.setItem(row_position, 2, QTableWidgetItem(str(reservation['NbPlaces'])))

    def search_reservation_action(self):
        reservation_number = self.reservation_number_input.text()
        if not reservation_number:
            QMessageBox.warning(self, "Champ vide", "Veuillez entrer un numéro de réservation.")
            return

        results = search_reservation_by_number(reservation_number)
        self.results_table.setRowCount(0)  # Réinitialiser la table

        for result in results:
            row_position = self.results_table.rowCount()
            self.results_table.insertRow(row_position)
            self.results_table.setItem(row_position, 0, QTableWidgetItem(result['Utilisateur']))
            self.results_table.setItem(row_position, 1, QTableWidgetItem(result['Film']))
            self.results_table.setItem(row_position, 2, QTableWidgetItem(str(result['NbPlaces'])))
