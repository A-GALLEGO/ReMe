import pygame
import tkinter as tk
from tkinter import ttk

class AudioPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_song_index = 0
        self.playing = False
        self.paused = False
        self.song_length = 0
        self.current_position = 0
        self.paused_position = 0
        
        pygame.init()

    def open_player(self):
        self.window = tk.Tk()
        self.window.title("Audio Player")
        self.window.geometry("500x400")

        # Handle window closure event
        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

        if self.playlist:
            self.window.configure(bg="lime green")
        else:
            self.window.configure(bg="red")

        self.song_label = tk.Label(self.window, text="Now Playing: ")
        self.song_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.window, length=400, mode='determinate')
        self.progress_bar.pack(pady=10)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        self.previous_button = tk.Button(button_frame, text="Previous", command=self.previous_song)
        self.previous_button.pack(side="left", padx=5)

        self.play_button = tk.Button(button_frame, text="Play", command=self.toggle_play_pause)
        self.play_button.pack(side="left", padx=5)

        # self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        # self.stop_button.pack(side="left", padx=5)

        self.next_button = tk.Button(button_frame, text="Next", command=self.next_song)
        self.next_button.pack(side="left", padx=5)

        self.window.mainloop()

    def on_window_close(self):
        self.stop_music()
        self.window.destroy()

    def toggle_play_pause(self):
        self.playing = not self.playing
        if self.playing:
            if self.paused:
                self.unpause_music()
            else:
                self.play_music()
        else:
            self.pause_music()


    def play_music(self):
        if not pygame.mixer.music.get_busy():
            song_path = self.playlist[self.current_song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.song_label.config(text="Now Playing: " + song_path)
            self.play_button.config(text="Pause")
            # self.stop_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.NORMAL)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.play_button.config(text="Play")
        self.paused_position = pygame.mixer.music.get_pos()
        self.paused = True

    def unpause_music(self):
        pygame.mixer.music.unpause()
        self.play_button.config(text="Pause")
        self.paused = False
        # pygame.mixer.music.set_pos(self.paused_position / 1000)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(text="Play")
        # self.progress_bar.stop()

    def next_song(self):
        self.stop_music()
        self.current_song_index += 1
        if self.current_song_index >= len(self.playlist):
            self.current_song_index = 0
        self.play_music()

    def previous_song(self):
        self.stop_music()
        self.current_song_index -= 1
        if self.current_song_index < 0:
            self.current_song_index = len(self.playlist) - 1
        self.play_music()

    pygame.quit()


if __name__ == "__main__":
    playlist = ["Song 1", "Song 2", "Song 3"]  # Replace with your actual playlist
    player = AudioPlayer(playlist)
    player.open_player()
