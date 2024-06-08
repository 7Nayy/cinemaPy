from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QDateEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QDate
from database import fetch_all_films, add_film
from edit_film_dialog import EditFilmDialog

class FilmTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Formulaire d'ajout de film
        self.form_layout = QFormLayout()
        self.titre_film_input = QLineEdit()
        self.description_film_input = QLineEdit()
        self.duree_film_input = QLineEdit()
        self.date_film_input = QDateEdit()
        self.date_film_input.setCalendarPopup(True)
        self.date_film_input.setDate(QDate.currentDate())
        self.form_layout.addRow("Titre du film:", self.titre_film_input)
        self.form_layout.addRow("Description:", self.description_film_input)
        self.form_layout.addRow("Durée (minutes):", self.duree_film_input)
        self.form_layout.addRow("Date de sortie:", self.date_film_input)

        self.submit_button = QPushButton("Ajouter le film")
        self.submit_button.clicked.connect(self.add_film_action)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.films_table = QTableWidget()
        self.films_table.setColumnCount(4)
        self.films_table.setHorizontalHeaderLabels(["Titre", "Description", "Durée", "Date de sortie"])
        layout.addWidget(self.films_table)

        self.setLayout(layout)
        self.load_films()

    def load_films(self):
        self.films_table.setRowCount(0)  # Réinitialiser la table
        films = fetch_all_films()
        for film in films:
            row_position = self.films_table.rowCount()
            self.films_table.insertRow(row_position)

            self.films_table.setItem(row_position, 0, QTableWidgetItem(film['Titre']))
            self.films_table.setItem(row_position, 1, QTableWidgetItem(film['Description']))
            self.films_table.setItem(row_position, 2, QTableWidgetItem(str(film['Durée'])))
            self.films_table.setItem(row_position, 3, QTableWidgetItem(film['DateSortie'].strftime('%Y-%m-%d')))

            # Bouton d'édition
            edit_button = QPushButton('Éditer')
            edit_button.clicked.connect(lambda _, film_id=film['Id']: self.edit_film_action(film_id))
            self.films_table.setCellWidget(row_position, 4, edit_button)

    def add_film_action(self):
        titre = self.titre_film_input.text()
        description = self.description_film_input.text()
        duree = self.duree_film_input.text()
        date_sortie = self.date_film_input.date().toString("yyyy-MM-dd")
        add_film(titre, description, duree, date_sortie)
        self.titre_film_input.clear()
        self.description_film_input.clear()
        self.duree_film_input.clear()
        self.load_films()

    def edit_film_action(self, film_id):
        dialog = EditFilmDialog(film_id, self)
        if dialog.exec_():
            self.load_films()
