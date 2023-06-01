import sqlite3
from Models.PlaylistSong import PlaylistSongs

class PlaylistSongRepository:
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
            CREATE TABLE IF NOT EXISTS playlistSongs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idSong TEXT,
                idPlaylist TEXT,
                FOREIGN KEY (idSong) REFERENCES songs (id),
                FOREIGN KEY (idPlaylist) REFERENCES playlists (id)
            )
        """)
        self.conn.commit()
        self.disconnect()

    def get_song_ids_by_playlist_id(self, playlist_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT idSong FROM playlistSongs WHERE idPlaylist = ?", (playlist_id,))
        rows = cursor.fetchall()
        self.disconnect()
        song_ids = [row[0] for row in rows]
        return song_ids

    def add_playlist_song(self, playlistsongs):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO playlistSongs (idSong, idPlaylist) VALUES (?, ?)",
                       (playlistsongs.idSong, playlistsongs.idPlaylist))
        self.conn.commit()
        self.disconnect()

    def get_playlist_ids_by_song_id(self, idSong):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT idPlaylist FROM playlistSongs WHERE idSong = ?", (idSong,))
        playlist_ids = cursor.fetchall()
        self.disconnect()

        return playlist_ids
