import sqlite3
from Models.Playlist import Playlists


class PlaylistRepository:
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
            CREATE TABLE IF NOT EXISTS playlists (
                id TEXT PRIMARY KEY,
                name TEXT
            )
        """)
        self.conn.commit()
        self.disconnect()

    def add_playlist(self, playlist):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO playlists (id, name)
            VALUES (?, ?)
        """, (playlist.id, playlist.name,))
        self.conn.commit()
        self.disconnect()

    def get_all_playlists(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM playlists")
        playlists = []
        rows = cursor.fetchall()
        for row in rows:
            playlist = Playlists(row[0], row[1])
            playlists.append(playlist)
        self.disconnect()
        return playlists

    def get_playlist_by_id(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM playlists WHERE id = ?", (id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            playlist = Playlists(row[0], row[1])
            return playlist
        return None
    
    def get_playlist_by_name(self, name):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM playlists WHERE name = ?", (name,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            playlist = Playlists(row[0], row[1])
            return playlist
        return None
    
    def get_playlistID_by_name(self, name):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM playlists WHERE name = ?", (name,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            playlist_id = row[0]
            return playlist_id
        return None
        

    def update_playlist(self, playlist):
        self.connect()
        cursor = self.conn.cursor()

        update_query = "UPDATE playlists SET name = ? WHERE id = ?"
        update_values = [playlist.name, playlist.id]

        cursor.execute(update_query, tuple(update_values))
        self.conn.commit()
        self.disconnect()

    def delete_playlist(self, id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM playlists WHERE id = ?", (id,))
        self.conn.commit()
        self.disconnect()