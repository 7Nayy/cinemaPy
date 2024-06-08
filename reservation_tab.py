from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QTableWidget, QTableWidgetItem
from database import fetch_all_reservations, add_reservation

class ReservationTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.form_layout = QFormLayout()
        self.utilisateur_input = QLineEdit()
        self.seance_input = QLineEdit()
        self.nb_places_input = QLineEdit()
        self.reservation_number_input = QLineEdit()

        self.form_layout.addRow("Utilisateur ID:", self.utilisateur_input)
        self.form_layout.addRow("Séance ID:", self.seance_input)
        self.form_layout.addRow("Nombre de Places:", self.nb_places_input)
        self.form_layout.addRow("Numéro de Réservation:", self.reservation_number_input)

        self.submit_button = QPushButton("Ajouter Réservation")
        self.submit_button.clicked.connect(self.add_reservation_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.reservations_table = QTableWidget()
        self.reservations_table.setColumnCount(5)
        self.reservations_table.setHorizontalHeaderLabels(["Utilisateur", "Film", "Séance ID", "Nombre de Places", "Numéro de Réservation"])
        layout.addWidget(self.reservations_table)

        self.setLayout(layout)
        self.update_reservations_display()

    def update_reservations_display(self):
        self.reservations_table.setRowCount(0)  # Réinitialiser la table
        reservations = fetch_all_reservations()
        for reservation in reservations:
            row_position = self.reservations_table.rowCount()
            self.reservations_table.insertRow(row_position)

            self.reservations_table.setItem(row_position, 0, QTableWidgetItem(reservation['Utilisateur']))
            self.reservations_table.setItem(row_position, 1, QTableWidgetItem(reservation['Film']))
            self.reservations_table.setItem(row_position, 2, QTableWidgetItem(str(reservation['SeanceId'])))
            self.reservations_table.setItem(row_position, 3, QTableWidgetItem(str(reservation['NbPlaces'])))
            self.reservations_table.setItem(row_position, 4, QTableWidgetItem(reservation['ReservationNumber']))

    def add_reservation_action(self):
        utilisateur_id = self.utilisateur_input.text()
        seance_id = self.seance_input.text()
        nb_places = self.nb_places_input.text()
        reservation_number = self.reservation_number_input.text()
        add_reservation(utilisateur_id, seance_id, nb_places, reservation_number)
        self.utilisateur_input.clear()
        self.seance_input.clear()
        self.nb_places_input.clear()
        self.reservation_number_input.clear()
        self.update_reservations_display()
