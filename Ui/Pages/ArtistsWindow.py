import tkinter as tk
from Repositories.ArtistRepository import ArtistRepository
from Services.Loader import Loader
from Services.AudioPlayer import AudioPlayer

class ArtistsWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.artist_repo = ArtistRepository("db.db")
        self.artist_listbox = tk.Listbox(self,  height=10)
        self.artist_listbox = None
        self.load_artists()
        

    def load_artists(self):
        self.artist_repo.create_table()
        artists = self.artist_repo.get_all_artists()
        
        if self.artist_listbox is not None:
            self.artist_listbox.destroy()

        self.artist_listbox = tk.Listbox(self, height=10)
        self.artist_listbox.pack(fill="both", expand=True)
        
        for artist in artists:
            self.artist_listbox.insert(tk.END, artist.name)
    # Bind double-click event to load songs to mixer
        self.artist_listbox.bind("<Double-Button-1>", lambda event: self.load_artist_songs_to_mixer(self.artist_listbox.get(tk.ACTIVE)))

        
    def load_artist_songs_to_mixer(self, artist_id):
        loader = Loader("db.db")  
        artist_songs = loader.load_songs_from_artist(artist_id)
        if artist_songs:
            player = AudioPlayer(artist_songs)
            player.open_player()





    def refresh(self):
        self.load_artists()
