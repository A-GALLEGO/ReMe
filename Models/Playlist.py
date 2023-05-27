

class Playlist:
    def __init__(self, playlist_id, name, songs):
        self.playlist_id = playlist_id
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"Playlist ID: {self.playlist_id}, Name: {self.name}, Songs: {', '.join(self.songs)}"

