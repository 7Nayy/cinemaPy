from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QDateEdit, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QDate
from database import get_film_by_id, update_film

class EditFilmDialog(QDialog):
    def __init__(self, film_id, parent=None):
        super(EditFilmDialog, self).__init__(parent)
        self.film_id = film_id
        self.setWindowTitle("Éditer Film")

        # Créer le formulaire d'édition
        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()

        self.titre_film_input = QLineEdit(self)
        self.description_film_input = QLineEdit(self)
        self.duree_film_input = QLineEdit(self)
        self.date_film_input = QDateEdit(self)
        self.date_film_input.setCalendarPopup(True)

        self.form_layout.addRow("Titre du film:", self.titre_film_input)
        self.form_layout.addRow("Description:", self.description_film_input)
        self.form_layout.addRow("Durée (minutes):", self.duree_film_input)
        self.form_layout.addRow("Date de sortie:", self.date_film_input)

        self.layout.addLayout(self.form_layout)

        # Boutons d'action
        self.buttons_layout = QHBoxLayout()
        self.save_button = QPushButton("Sauvegarder", self)
        self.cancel_button = QPushButton("Annuler", self)

        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.buttons_layout)

        self.save_button.clicked.connect(self.save_changes)
        self.cancel_button.clicked.connect(self.reject)

        self.load_film_details()

    def load_film_details(self):
        film = get_film_by_id(self.film_id)
        if film:
            self.titre_film_input.setText(film['Titre'])
            self.description_film_input.setText(film['Description'])
            self.duree_film_input.setText(str(film['Durée']))
            # Assurez-vous que la date est au format attendu (YYYY-MM-DD)
            date_film = QDate.fromString(film['DateSortie'], "yyyy-MM-dd")
            self.date_film_input.setDate(date_film)

    def save_changes(self):
        titre = self.titre_film_input.text()
        description = self.description_film_input.text()
        duree = self.duree_film_input.text()
        date_sortie = self.date_film_input.date().toString("yyyy-MM-dd")
        update_film(self.film_id, titre, description, duree, date_sortie)
        self.accept()
