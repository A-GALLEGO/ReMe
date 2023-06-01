class PlaylistSongs:
    def __init__(self, idSong=None, idPlaylist=None):
        self.idSong = idSong
        self.idPlaylist = idPlaylist

    def __str__(self):
        return f"Song ID: {self.idSong}, Playlist ID: {self.idPlaylist}"