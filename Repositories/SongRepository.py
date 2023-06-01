import sqlite3
from Models.Song import Songs

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
                id TEXT PRIMARY KEY,
                name TEXT,
                idArtist TEXT,
                duration TEXT,
                filePath TEXT
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_song(self, song):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO songs (id, name, idArtist, duration, filePath)
            VALUES (?, ?, ?, ?, ?)
        """, (song.id, song.name, song.idArtist, song.duration, song.filePath,))
        self.conn.commit()
        self.disconnect()

    def get_all_songs(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM songs")
        songs = []
        rows = cursor.fetchall()
        for row in rows:
            song = Songs(row[0], row[1], row[2], row[3], row[4])
            songs.append(song)
        self.disconnect()
        return songs

    def get_song_by_id(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM songs WHERE id = ?", (id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            song = Songs(row[0], row[1], row[2], row[3], row[4])
            return song
        return None
    
    def get_song_path_by_id(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT filePath FROM songs WHERE id = ?", (id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return row[0]
        return None
    
    def get_song_path_by_artist_id(self, artist_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT filePath FROM songs WHERE idArtist = ?", (artist_id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return row[0]
        return None

    def update_song(self, song):
        self.connect()
        cursor = self.conn.cursor()

        update_query = "UPDATE songs SET name = ?, idArtist = ?, duration = ?, filePath = ? WHERE id = ?"
        update_values = [song.name, song.idArtist, song.duration, song.filePath, song.id]

        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()
    
    
    def update_song_path(self, song):
        self.connect()
        cursor = self.conn.cursor()
    
        update_query = "UPDATE songs SET filePath = ? WHERE id = ?"
        update_values = [song.filePath, song.id]
    
        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()


    def delete_song(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM songs WHERE id = ?", (id,))
        self.conn.commit()
        self.disconnect()
