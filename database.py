# database.py
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

def add_film(nom, date):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Film (Nom, Date) VALUES (%s, %s)"
            cursor.execute(sql, (nom, date))
        conn.commit()
    finally:
        conn.close()

def fetch_all_reservations():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT Reserver.UtilisateurId, Utilisateur.Nom AS Utilisateur, Film.Nom AS Film, Reserver.FilmId
            FROM Reserver
            JOIN Utilisateur ON Reserver.UtilisateurId = Utilisateur.Id
            JOIN Film ON Reserver.FilmId = Film.Id
            """
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def add_reservation(utilisateur_id, film_id):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Reserver (UtilisateurId, FilmId) VALUES (%s, %s)"
            cursor.execute(sql, (utilisateur_id, film_id))
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

def update_film(film_id, nom, date):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Film SET Nom = %s, Date = %s WHERE Id = %s"
            cursor.execute(sql, (nom, date, film_id))
        conn.commit()
    finally:
        conn.close()

def delete_film(film_id):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM Film WHERE Id = %s"
            cursor.execute(sql, (film_id,))
        conn.commit()
    finally:
        conn.close()

def get_film_by_id(film_id):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Film WHERE Id = %s"
            cursor.execute(sql, (film_id,))
            return cursor.fetchone()  # Retourne un seul enregistrement
    finally:
        conn.close()

