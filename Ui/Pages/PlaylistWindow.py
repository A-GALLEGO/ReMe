import tkinter as tk
from Repositories.PlaylistRepository import PlaylistRepository
from Services.Loader import Loader
from Services.AudioPlayer import AudioPlayer


class PlaylistWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.playlist_repo = PlaylistRepository("db.db")  # Replace "db.db" with the actual path to your database file
        self.playlist_listbox = tk.Listbox(self,  height=10)
        self.playlist_listbox = None
        self.load_playlists()  
        


    def load_playlists(self):
        self.playlist_repo.create_table()
        playlists = self.playlist_repo.get_all_playlists()
        
        if self.playlist_listbox is not None:
            self.playlist_listbox.destroy()

        self.playlist_listbox = tk.Listbox(self, height=10)
        self.playlist_listbox.pack(fill="both", expand=True)
        
        for playlist in playlists:
            self.playlist_listbox.insert(tk.END, playlist.name)
    # Bind double-click event to load songs to mixer
        self.playlist_listbox.bind("<Double-Button-1>", lambda event: self.load_playlist_songs_to_mixer(self.playlist_listbox.get(tk.ACTIVE)))
        
    def load_playlist_songs_to_mixer(self, playlist_name):
        loader = Loader("db.db")  # Replace "db.db" with the actual path to your database file
        playlist = loader.load_songs_from_playlist(playlist_name)
        print(playlist)
        if playlist:
            # Create an instance of the AudioPlayer with the playlist
            player = AudioPlayer(playlist)
            player.open_player()

    def refresh(self):
        self.load_playlists()
