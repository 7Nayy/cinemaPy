from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from database import connect_to_database

class CinemaSalleTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.setLayout(layout)
        self.display_cinemas(layout)

    def display_cinemas(self, layout):
        conn = connect_to_database()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM Cinema"
                cursor.execute(sql)
                cinemas = cursor.fetchall()

                for cinema in cinemas:
                    layout.addWidget(
                        QLabel(f"Nom: {cinema['Nom']}, Adresse: {cinema['Adresse']}"))
        finally:
            conn.close()
