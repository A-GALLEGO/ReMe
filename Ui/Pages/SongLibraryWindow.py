import tkinter as tk
import pygame
from Repositories.SongRepository import SongRepository
from Services.Loader import Loader
from Services.AudioPlayer import AudioPlayer

class SongLibraryWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.song_repo = SongRepository("db.db")
        self.song_listbox = None
        self.load_songs()
        
        
        # Create a frame for the play button
        play_button_frame = tk.Frame(self)
        play_button_frame.pack(side="top", padx=10, pady=10)
        # Create the "Play" button
        # play_button = tk.Button(play_button_frame, text="Play", command = self.load_song_library_to_mixer)
        # play_button.pack(side="left")

    def load_songs(self):
        self.song_repo.create_table()
        songs = self.song_repo.get_all_songs()

        if self.song_listbox is not None:
            self.song_listbox.destroy()

        self.song_listbox = tk.Listbox(self, height=10)  # Adjust the height value as needed
        self.song_listbox.pack(fill="both", expand=True)

        for song in songs:
            self.song_listbox.insert(tk.END, song.name)
    
    # def load_song_library_to_mixer(self, playlist):
    #     loader = Loader("db.db")
    #     songs = loader.load_all_songs()
    #     if songs:
    #         player = AudioPlayer(songs)
    #         player.open_player()



    def refresh(self):
        self.load_songs()

