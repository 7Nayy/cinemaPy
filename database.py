import pymysql

def connect_to_database():
    return pymysql.connect(host='212.132.116.22',
                           user='root',
                           password='admin719',
                           db='cinema',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def fetch_all_films():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Film"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def get_film_by_id(film_id):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Film WHERE Id = %s"
            cursor.execute(sql, (film_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def add_film(titre, description, duree, date_sortie):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Film (Titre, Description, Durée, DateSortie) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (titre, description, duree, date_sortie))
        conn.commit()
    finally:
        conn.close()

def fetch_all_reservations():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT Reservation.Id, Reservation.UtilisateurId, Reservation.SeanceId, Reservation.NbPlaces, 
                   Reservation.ReservationNumber, Film.Titre AS Film, Utilisateur.Nom AS Utilisateur
            FROM Reservation
            JOIN Film ON Reservation.SeanceId = Film.Id
            JOIN Utilisateur ON Reservation.UtilisateurId = Utilisateur.Id
            """
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()


def add_reservation(utilisateur_id, seance_id, nb_places, reservation_number):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Reservation (UtilisateurId, SeanceId, NbPlaces, ReservationNumber) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (utilisateur_id, seance_id, nb_places, reservation_number))
        conn.commit()
    finally:
        conn.close()

def fetch_all_users():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT Id, Nom FROM Utilisateur ORDER BY Nom"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def update_film(film_id, titre, description, duree, date_sortie):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Film SET Titre = %s, Description = %s, Durée = %s, DateSortie = %s WHERE Id = %s"
            cursor.execute(sql, (titre, description, duree, date_sortie, film_id))
        conn.commit()
    finally:
        conn.close()

def fetch_all_seances():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT Seance.Id, Seance.DateTimeSeance, Film.Titre AS Film, Salle.Numero AS Salle
            FROM Seance
            JOIN Film ON Seance.FilmId = Film.Id
            JOIN Salle ON Seance.SalleId = Salle.Id
            """
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def add_seance(film_id, date_heure, salle_id):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Seance (FilmId, DateTimeSeance, SalleId) VALUES (%s, %s, %s)"
            cursor.execute(sql, (film_id, date_heure, salle_id))
        conn.commit()
    finally:
        conn.close()
