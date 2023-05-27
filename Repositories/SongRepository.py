import sqlite3

class SongRepository:
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
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                artist TEXT,
                duration INTEGER
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_song(self, title, artist, duration):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO songs (title, artist, duration)
            VALUES (?, ?, ?)
        """, (title, artist, duration))
        self.conn.commit()
        self.disconnect()

    def get_all_songs(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()
        self.disconnect()
        return songs

    def get_song_by_id(self, song_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM songs WHERE id = ?", (song_id,))
        song = cursor.fetchone()
        self.disconnect()
        return song

    def update_song(self, song_id, title=None, artist=None, duration=None):
        self.connect()
        cursor = self.conn.cursor()

        update_query = "UPDATE songs SET"
        update_values = []

        if title:
            update_query += " title = ?,"
            update_values.append(title)
        if artist:
            update_query += " artist = ?,"
            update_values.append(artist)
        if duration:
            update_query += " duration = ?,"
            update_values.append(duration)

        # Remove the trailing comma from the query
        update_query = update_query.rstrip(',')

        update_query += " WHERE id = ?"
        update_values.append(song_id)

        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()

    def delete_song(self, song_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM songs WHERE id = ?", (song_id,))
        self.conn.commit()
        self.disconnect()
