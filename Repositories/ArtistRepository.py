import sqlite3
from Models.Artist import Artist



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
                id TEXT PRIMARY KEY,
                name TEXT
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_artist(self, artist):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO artists (id, name)
            VALUES (?, ?)
        """, (artist.id, artist.name,))
        self.conn.commit()
        self.disconnect()

    def get_all_artists(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM artists")
        artists = []
        rows = cursor.fetchall()
        for row in rows:
            artist = Artist.init_from_db_row(row)
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
            return Artist.init_from_db_row(row)
        return None
    
    def get_artist_by_name(self, artist_name):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM artists WHERE name=?", (artist_name,))
        artist = cursor.fetchone()
        connection.close()
        return artist
    
    def get_artist_id_by_name(self, artist_name):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM artists WHERE name = ?", (artist_name,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return result[0]
        else:
            return None

    def update_artist(self, artist):
        self.connect()
        cursor = self.conn.cursor()

        update_query = "UPDATE artists SET name = ? WHERE id = ?"
        update_values = [artist.name, artist.id]

        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()

    def delete_artist(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM artists WHERE id = ?", (id,))
        self.conn.commit()
        self.disconnect()
