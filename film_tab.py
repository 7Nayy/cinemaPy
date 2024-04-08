# Modifications dans film_tab.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QDateEdit, QDialog, \
    QTableWidgetItem
from PyQt5.QtCore import QDate
from database import fetch_all_films, add_film
from edit_film_dialog import EditFilmDialog



class FilmTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Formulaire d'ajout de film
        self.form_layout = QFormLayout()
        self.nom_film_input = QLineEdit()
        self.date_film_input = QDateEdit()
        self.date_film_input.setCalendarPopup(True)
        self.date_film_input.setDate(QDate.currentDate())
        self.form_layout.addRow("Nom du film:", self.nom_film_input)
        self.form_layout.addRow("Date de sortie:", self.date_film_input)

        self.submit_button = QPushButton("Ajouter le film")
        self.submit_button.clicked.connect(self.add_film_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

    def load_films(self):
        self.films_table.setRowCount(0)  # Réinitialiser la table
        films = fetch_all_films()
        for film in films:
            row_position = self.films_table.rowCount()
            self.films_table.insertRow(row_position)

            self.films_table.setItem(row_position, 0, QTableWidgetItem(film['Nom']))
            self.films_table.setItem(row_position, 1, QTableWidgetItem(film['Date'].strftime('%Y-%m-%d')))

            # Bouton d'édition
            edit_button = QPushButton('Éditer')
            edit_button.clicked.connect(lambda _, film_id=film['Id']: self.edit_film_action(film_id))
            self.films_table.setCellWidget(row_position, 2, edit_button)

    def add_film_action(self):
        nom = self.nom_film_input.text()
        date = self.date_film_input.date().toString("yyyy-MM-dd")
        add_film(nom, date)
        self.nom_film_input.clear()
        # Mettre à jour l'affichage des films ici

    def edit_film_action(self, film_id):
        dialog = EditFilmDialog(film_id)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            self.load_films()  # Recharger les films après l'édition