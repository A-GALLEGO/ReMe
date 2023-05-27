import sqlite3
from ReMe2.Models.Artist import Artist



class ArtistRepository:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_artist(self, name):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO artists (name)
            VALUES (?)
        """, (name,))
        self.conn.commit()
        id = cursor.lastrowid  # Get the auto-incremented ID of the inserted row
        self.disconnect()
        return Artist(id, name)

    def get_all_artists(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM artists")
        artists = []
        rows = cursor.fetchall()
        for row in rows:
            artist = Artist(row[0], row[1])
            artists.append(artist)
        self.disconnect()
        return artists

    def get_artist_by_id(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM artists WHERE id = ?", (id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return Artist(row[0], row[1])
        return None

    def update_artist(self, artist):
        self.connect()
        cursor = self.conn.cursor()

        update_query = "UPDATE artists SET"
        update_values = []

        if artist.name:
            update_query += " name = ?,"
            update_values.append(artist.name)

        # Remove the trailing comma from the query
        update_query = update_query.rstrip(',')

        update_query += " WHERE id = ?"
        update_values.append(artist.id)

        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()

    def delete_artist(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM artists WHERE id = ?", (id,))
        self.conn.commit()
        self.disconnect()
