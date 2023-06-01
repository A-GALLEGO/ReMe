import pygame
import tkinter as tk
from tkinter import messagebox

class PlayerWindow:
    def __init__(self, song_title, song_duration):
        pygame.init()
        pygame.mixer.init()
        self.screen_width = 400
        self.screen_height = 150
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Music Player")

        self.song_title = song_title
        self.song_duration = song_duration

        self.clock = pygame.time.Clock()
        self.is_playing = False

        self.load_assets()

    def load_assets(self):
        # Load images
        self.play_button_img = pygame.image.load("play_button.png")
        self.pause_button_img = pygame.image.load("pause_button.png")
        self.prev_button_img = pygame.image.load("previous_button.png")
        self.next_button_img = pygame.image.load("next_button.png")

        # Resize images
        button_size = (50, 50)
        self.play_button_img = pygame.image.load("C:/Users/galle/Documents/GitHub/ReMe/Assets/Artwork/play-16.png")
        self.pause_button_img = pygame.image.load("C:/Users/galle/Documents/GitHub/ReMe/Assets/Artwork/pause-16.png")
        self.prev_button_img = pygame.image.load("C:/Users/galle/Documents/GitHub/ReMe/Assets/Artwork/previous-16.png")
        self.next_button_img = pygame.image.load("C:/Users/galle/Documents/GitHub/ReMe/Assets/Artwork/next-16.png")

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw_ui(self):
        # Draw song title
        title_font = pygame.font.Font(None, 20)
        title_text = title_font.render(self.song_title, True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 30))
        self.screen.blit(title_text, title_rect)

        # Draw play/pause button
        button_img = self.pause_button_img if self.is_playing else self.play_button_img
        button_rect = button_img.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(button_img, button_rect)

        # Draw previous button
        prev_button_rect = self.prev_button_img.get_rect(center=(self.screen_width // 2 - 50, self.screen_height // 2))
        self.screen.blit(self.prev_button_img, prev_button_rect)

        # Draw next button
        next_button_rect = self.next_button_img.get_rect(center=(self.screen_width // 2 + 50, self.screen_height // 2))
        self.screen.blit(self.next_button_img, next_button_rect)

        # Draw song duration
        duration_font = pygame.font.Font(None, 16)
        duration_text = duration_font.render(self.song_duration, True, (0, 0, 0))
        duration_rect = duration_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 30))
        self.screen.blit(duration_text, duration_rect)

        # Add functionality for button clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if button_rect.collidepoint(mouse_pos) and mouse_clicked:
            self.is_playing = not self.is_playing

        # Add functionality for previous button and next button

class PlayMusic:
    def __init__(self, song_list):
        self.song_list = song_list
        self.current_song_index = 0
        self.player_window = None

    def play_selected_song(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def play_all_songs(self):
        if not self.song_list:
            messagebox.showinfo("No Songs", "No songs in the list.")
            return

        self.play_selected_song(self.song_list[self.current_song_index])
        self.show_player_window()

    def show_player_window(self):
        song_title = self.get_song_title(self.song_list[self.current_song_index])
        song_duration = "5:00"  # Replace with the actual song duration
        self.player_window = PlayerWindow(song_title, song_duration)
        self.player_window.run()

    def get_song_title(self, song_path):
        song_title = song_path.split("/")[-1].split(".")[0]
        return song_title

    # Add functionality for previous button and next button
