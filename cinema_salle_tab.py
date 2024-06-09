from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
from database import fetch_all_cinemas, add_cinema, fetch_salles_by_cinema, add_salle

class CinemaSalleTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Formulaire d'ajout de cinéma
        self.cinema_form_layout = QFormLayout()
        self.cinema_nom_input = QLineEdit()
        self.cinema_adresse_input = QLineEdit()
        self.cinema_form_layout.addRow("Nom du cinéma:", self.cinema_nom_input)
        self.cinema_form_layout.addRow("Adresse:", self.cinema_adresse_input)

        self.cinema_submit_button = QPushButton("Ajouter Cinéma")
        self.cinema_submit_button.clicked.connect(self.add_cinema_action)
        layout.addLayout(self.cinema_form_layout)
        layout.addWidget(self.cinema_submit_button)

        # Liste déroulante pour sélectionner un cinéma
        self.cinema_combobox = QComboBox()
        self.cinema_combobox.currentIndexChanged.connect(self.update_salles_display)
        layout.addWidget(self.cinema_combobox)

        # Formulaire d'ajout de salle
        self.salle_form_layout = QFormLayout()
        self.salle_numero_input = QLineEdit()
        self.salle_capacite_input = QLineEdit()
        self.salle_form_layout.addRow("Numéro de la salle:", self.salle_numero_input)
        self.salle_form_layout.addRow("Capacité de la salle:", self.salle_capacite_input)

        self.salle_submit_button = QPushButton("Ajouter Salle")
        self.salle_submit_button.clicked.connect(self.add_salle_action)
        layout.addLayout(self.salle_form_layout)
        layout.addWidget(self.salle_submit_button)

        # Table pour afficher les salles
        self.salles_table = QTableWidget()
        self.salles_table.setColumnCount(2)
        self.salles_table.setHorizontalHeaderLabels(["Numéro de Salle", "Capacité"])
        layout.addWidget(self.salles_table)

        self.setLayout(layout)
        self.update_cinemas_display()

    def update_cinemas_display(self):
        self.cinema_combobox.clear()
        cinemas = fetch_all_cinemas()
        for cinema in cinemas:
            self.cinema_combobox.addItem(cinema['Nom'], cinema['Id'])

    def update_salles_display(self):
        self.salles_table.setRowCount(0)
        cinema_id = self.cinema_combobox.currentData()
        if cinema_id:
            salles = fetch_salles_by_cinema(cinema_id)
            for salle in salles:
                row_position = self.salles_table.rowCount()
                self.salles_table.insertRow(row_position)
                self.salles_table.setItem(row_position, 0, QTableWidgetItem(str(salle['Numero'])))
                self.salles_table.setItem(row_position, 1, QTableWidgetItem(str(salle['Capacité'])))

    def add_cinema_action(self):
        nom = self.cinema_nom_input.text()
        adresse = self.cinema_adresse_input.text()

        if not nom or not adresse:
            QMessageBox.warning(self, "Champs vides", "Tous les champs doivent être remplis.")
            return

        add_cinema(nom, adresse)
        self.cinema_nom_input.clear()
        self.cinema_adresse_input.clear()
        self.update_cinemas_display()

    def add_salle_action(self):
        numero = self.salle_numero_input.text()
        capacite = self.salle_capacite_input.text()
        cinema_id = self.cinema_combobox.currentData()

        if not numero or not capacite or cinema_id is None:
            QMessageBox.warning(self, "Champs vides", "Tous les champs doivent être remplis.")
            return

        add_salle(cinema_id, numero, capacite)
        self.salle_numero_input.clear()
        self.salle_capacite_input.clear()
        self.update_salles_display()
