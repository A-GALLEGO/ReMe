import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial
import PlaylistRepository

class PlaylistPage:
    def __init__(self, playlist_repo):
        self.playlist_repo = playlist_repo

    def show_playlists(self):
        playlists = self.playlist_repo.get_all_playlists()

        # Create the main window
        window = tk.Tk()
        window.title("List of Playlists")

        # Create a Treeview widget to display the playlists
        tree = ttk.Treeview(window)
        tree["columns"] = ("name", "songs")
        tree.column("name", width=200, anchor="center")
        tree.column("songs", width=300, anchor="w")
        tree.heading("name", text="Name")
        tree.heading("songs", text="Songs")

        # Populate the Treeview with the playlists
        for playlist in playlists:
            tree.insert("", tk.END, text=playlist.playlist_id, values=(playlist.name, ", ".join(playlist.songs)))

        tree.pack(padx=10, pady=10)

        # Function to handle selection
        def handle_selection(event):
            selected_item = tree.selection()[0]
            playlist_id = tree.item(selected_item, "text")
            showinfo("Selected Playlist", f"Playlist ID: {playlist_id}")

        # Bind the selection event
        tree.bind("<<TreeviewSelect>>", handle_selection)

        window.mainloop()


# Usage example
playlist_repo = PlaylistRepository('playlists.db', Playlist)

# Create some sample playlists
playlist_repo.add_playlist("Playlist 1", ["Song 1", "Song 2", "Song 3"])
playlist_repo.add_playlist("Playlist 2", ["Song 4", "Song 5", "Song 6"])

# Create an instance of the PlaylistPage and show the playlists
page = PlaylistPage(playlist_repo)
page.show_playlists()
