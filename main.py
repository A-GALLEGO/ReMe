import tkinter as tk
from Ui.Pages.MainMenu import MainMenuWindow
import pygame
from Services.Loader import Loader
from Repositories.SongRepository import SongRepository


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.geometry("400x300")  # Set the width and height as desired
    root.title("Reme Application")

    main_menu_window = MainMenuWindow(root)
    main_menu_window.pack(fill="both", expand=True)
    
    # song_repository = SongRepository('db.db')

    # # Retrieve the song you want to update
    # song_id = 'your_song_id'
    # song = song_repository.get_song_by_id(song_id)

    # if song:
    #     # Update the filePath attribute of the song with the new path
    #     new_file_path = 'new/path/to/song.mp3'
    #     song.filePath = new_file_path

    #     # Call the update_song_path function to update the song's path in the database
    #     song_repository.update_song_path(song)
    #     print("Song path updated successfully.")
    # else:
    #     print("Song not found.")

    # # Disconnect from the database
    # song_repository.disconnect()
    
    root.mainloop()
