import tkinter as tk
import tkinter.ttk as ttk
from Ui.Pages.PlaylistWindow import PlaylistWindow
from Ui.Pages.ArtistsWindow import ArtistsWindow
from Ui.Pages.SongLibraryWindow import SongLibraryWindow

class MainMenuWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.notebook = ttk.Notebook(self)

        self.playlist_window = PlaylistWindow(self.notebook)
        self.notebook.add(self.playlist_window, text="Playlist")

        self.artists_window = ArtistsWindow(self.notebook)
        self.notebook.add(self.artists_window, text="Artists")

        self.song_library_window = SongLibraryWindow(self.notebook)
        self.notebook.add(self.song_library_window, text="Song Library")

        self.notebook.bind("<<NotebookTabChanged>>", self.refresh_current_window)

        self.notebook.pack(fill="both", expand=True)

    def refresh_current_window(self, event):
        selected_tab = self.notebook.tab(self.notebook.select(), "text")
        if selected_tab == "Playlist":
            self.playlist_window.refresh()
        elif selected_tab == "Artists":
            self.artists_window.refresh()
        elif selected_tab == "Song Library":
            self.song_library_window.refresh()
