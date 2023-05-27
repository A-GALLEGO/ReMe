import sqlite3

class PlaylistRepository:
    def __init__(self, db_file, playlist_model):
        self.db_file = db_file
        self.playlist_model = playlist_model
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
            CREATE TABLE IF NOT EXISTS playlists (
                playlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                songs TEXT
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_playlist(self, name, songs):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO playlists (name, songs)
            VALUES (?, ?)
        """, (name, ', '.join(songs)))
        self.conn.commit()
        self.disconnect()

    def get_all_playlists(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM playlists")
        playlists = []
        rows = cursor.fetchall()
        for row in rows:
            playlist = self.playlist_model(row[0], row[1], row[2].split(', '))
            playlists.append(playlist)
        self.disconnect()
        return playlists

    def get_playlist_by_id(self, playlist_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM playlists WHERE playlist_id = ?", (playlist_id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return self.playlist_model(row[0], row[1], row[2].split(', '))
        return None

    def update_playlist(self, playlist):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("UPDATE playlists SET name = ?, songs = ? WHERE playlist_id = ?",
                       (playlist.name, ', '.join(playlist.songs), playlist.playlist_id))
        self.conn.commit()
        self.disconnect()

    def delete_playlist(self, playlist_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM playlists WHERE playlist_id = ?", (playlist_id,))
        self.conn.commit()
        self.disconnect()
