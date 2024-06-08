from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QDateTimeEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QDateTime
from database import fetch_all_seances, add_seance

class SeanceTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.form_layout = QFormLayout()
        self.film_id_input = QLineEdit()
        self.date_heure_input = QDateTimeEdit()
        self.date_heure_input.setCalendarPopup(True)
        self.date_heure_input.setDateTime(QDateTime.currentDateTime())
        self.salle_id_input = QLineEdit()

        self.form_layout.addRow("Film ID:", self.film_id_input)
        self.form_layout.addRow("Date et Heure:", self.date_heure_input)
        self.form_layout.addRow("Salle ID:", self.salle_id_input)

        self.submit_button = QPushButton("Ajouter Séance")
        self.submit_button.clicked.connect(self.add_seance_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.seances_table = QTableWidget()
        self.seances_table.setColumnCount(3)
        self.seances_table.setHorizontalHeaderLabels(["Film", "Date et Heure", "Salle"])
        layout.addWidget(self.seances_table)

        self.setLayout(layout)
        self.update_seances_display()

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
        film_id = self.film_id_input.text()
        date_heure = self.date_heure_input.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        salle_id = self.salle_id_input.text()
        add_seance(film_id, date_heure, salle_id)
        self.film_id_input.clear()
        self.salle_id_input.clear()
        self.update_seances_display()
