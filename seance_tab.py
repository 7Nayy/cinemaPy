from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QDateTimeEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QDateTime
from database import fetch_all_seances, add_seance, fetch_all_films, fetch_all_salles

class SeanceTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Formulaire d'ajout de séance
        self.form_layout = QFormLayout()

        self.film_combobox = QComboBox()
        self.date_heure_input = QDateTimeEdit()
        self.date_heure_input.setCalendarPopup(True)
        self.date_heure_input.setDateTime(QDateTime.currentDateTime())
        self.salle_combobox = QComboBox()

        self.form_layout.addRow("Film:", self.film_combobox)
        self.form_layout.addRow("Date et Heure:", self.date_heure_input)
        self.form_layout.addRow("Salle:", self.salle_combobox)

        self.submit_button = QPushButton("Ajouter Séance")
        self.submit_button.clicked.connect(self.add_seance_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        # Table pour afficher les séances
        self.seances_table = QTableWidget()
        self.seances_table.setColumnCount(3)
        self.seances_table.setHorizontalHeaderLabels(["Film", "Date et Heure", "Salle"])
        layout.addWidget(self.seances_table)

        self.setLayout(layout)
        self.load_films_and_salles()
        self.update_seances_display()

    def load_films_and_salles(self):
        # Charger les films dans la combobox
        films = fetch_all_films()
        self.film_combobox.clear()
        for film in films:
            self.film_combobox.addItem(film['Titre'], film['Id'])

        # Charger les salles dans la combobox
        salles = fetch_all_salles()
        self.salle_combobox.clear()
        for salle in salles:
            salle_label = f"{salle['CinemaNom']} - Salle {salle['Numero']}"
            self.salle_combobox.addItem(salle_label, salle['Id'])

    def update_seances_display(self):
        self.seances_table.setRowCount(0)  # Réinitialiser la table
        seances = fetch_all_seances()
        for seance in seances:
            row_position = self.seances_table.rowCount()
            self.seances_table.insertRow(row_position)
            self.seances_table.setItem(row_position, 0, QTableWidgetItem(seance['Film']))
            self.seances_table.setItem(row_position, 1, QTableWidgetItem(seance['DateTimeSeance'].strftime('%Y-%m-%d %H:%M')))
            self.seances_table.setItem(row_position, 2, QTableWidgetItem(seance['Salle']))

    def add_seance_action(self):
        film_id = self.film_combobox.currentData()
        date_heure = self.date_heure_input.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        salle_id = self.salle_combobox.currentData()

        if not film_id or not date_heure or not salle_id:
            QMessageBox.warning(self, "Champs vides", "Tous les champs doivent être remplis.")
            return

        add_seance(film_id, date_heure, salle_id)
        self.update_seances_display()
