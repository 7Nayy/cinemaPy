from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QFormLayout
from database import fetch_all_reservations, add_reservation, fetch_all_films, fetch_all_users

class ReservationTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Ajouter le formulaire de réservation
        self.form_layout = QFormLayout()
        self.utilisateur_input = QComboBox()
        self.film_input = QComboBox()

        utilisateurs = fetch_all_users()
        for utilisateur in utilisateurs:
            self.utilisateur_input.addItem(utilisateur['Nom'], utilisateur['Id'])

        films = fetch_all_films()
        for film in films:
            self.film_input.addItem(film['Nom'], film['Id'])

        self.form_layout.addRow("Utilisateur:", self.utilisateur_input)
        self.form_layout.addRow("Film:", self.film_input)

        self.submit_button = QPushButton("Ajouter Réservation")
        self.submit_button.clicked.connect(self.add_reservation_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        # Afficher les réservations existantes
        self.reservations_label = QVBoxLayout()
        self.update_reservations_display()
        layout.addLayout(self.reservations_label)

    # Les fonctions add_reservation_action et update_reservations_display vont ici

    def add_reservation_action(self):
        utilisateur_id = self.utilisateur_input.currentData()
        film_id = self.film_input.currentData()
        add_reservation(utilisateur_id, film_id)
        self.update_reservations_display()

    def update_reservations_display(self):
        # Nettoyer les anciennes réservations affichées
        while self.reservations_label.count():
            child = self.reservations_label.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        reservations = fetch_all_reservations()
        for reservation in reservations:
            self.reservations_label.addWidget(
                QLabel(f"Utilisateur: {reservation['Utilisateur']}, Film: {reservation['Film']}"))
