import pygame
from Repositories.SongRepository import SongRepository
from Repositories.ArtistRepository import ArtistRepository
from Repositories.PlaylistRepository import PlaylistRepository
from Repositories.PlaylistSongRepository import PlaylistSongRepository

class Loader:
    def __init__(self, db_file):
        #Initialize pygame mixer
        pygame.mixer.init()

        self.db_file = db_file
        self.song_repo = SongRepository(self.db_file)
        self.playlist_repo = PlaylistRepository(self.db_file)
        self.playlist_song_repo = PlaylistSongRepository(self.db_file)
        self.artist_repo = ArtistRepository(self.db_file)

    def load_songs_from_playlist(self, playlist_name):
        song_repo = SongRepository(self.db_file)
        song_repo.create_table()
        playlist_id = self.playlist_repo.get_playlistID_by_name(playlist_name)
        # print(playlist_id)
        if playlist_id:
            song_ids = self.playlist_song_repo.get_song_ids_by_playlist_id(playlist_id)
            playlist = []
            for song_id in song_ids:
                song_path = song_repo.get_song_path_by_id(song_id)
                if song_path:
                    playlist.append(song_path)  # Append the song path to the playlist
                    # pygame.mixer.music.load(song_path)
                    # print("Loaded song:", song_id, song_path)
        return playlist  # Return the constructed playlist

    def load_songs_from_artist(self, selected_artist):
        artist_repo = ArtistRepository(self.db_file)
        artist_repo.create_table()
        artist_id = artist_repo.get_artist_id_by_name(selected_artist)
        if artist_id:
            artist_id = str(artist_id)  # Convert artist_id to a string
            print(artist_id)
            artist_songs = []
            all_songs = self.song_repo.get_all_songs()
            for song in all_songs:
                if song.idArtist == artist_id:
                    artist_songs.append(song.filePath)
                    pygame.mixer.music.load(song.filePath)
                    print("Loaded song:", artist_id, song.filePath)
        else:
            artist_songs = []
        return artist_songs  # Return the constructed playlist
    
    def load_all_songs(self):
        self.song_repo.create_table()
        songs = self.song_repo.get_all_songs()
        playlist = []

        for song in songs:
            song_path = song.filePath
            playlist.append(song_path)
            pygame.mixer.music.load(song_path)
            print("Loaded song:", song.id, song_path)
        return playlist
    
    def load_songs_to_mixer(self):
        self.song_repo.create_table()
        songs = self.song_repo.get_all_songs()

        for song in songs:
            song_path = self.song_repo.get_song_path_by_id()
            pygame.mixer.music.load(song_path)
            # print("Loaded song:", song.id, song_path)

