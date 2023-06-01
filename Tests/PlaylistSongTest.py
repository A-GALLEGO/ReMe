import unittest
import tempfile
import os
from Repositories.PlaylistSongRepository import PlaylistSongRepository
from Models.PlaylistSong import PlaylistSongs

class PlaylistSongsRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mktemp()  # Create a temporary database file
        self.repository = PlaylistSongRepository(self.db_file)
        self.repository.create_table()

    def tearDown(self):
        self.repository.disconnect()
        os.remove(self.db_file)

    def test_add_playlist_song(self):
        playlist_song = PlaylistSongs(1, 1)  # Assuming playlist_id and song_id are 1
        self.repository.add_playlist_song(PlaylistSongs)
        songs = self.repository.get_songs_by_playlist_id(1)  # Assuming playlist_id is 1
        self.assertIn(1, songs)  # Assuming song_id is 1

    def test_get_songs_by_playlist_id(self):
        playlist_song1 = PlaylistSongs(1, 1)  # Assuming playlist_id and song_id are 1
        playlist_song2 = PlaylistSongs(1, 2)  # Assuming playlist_id is 1 and song_id is 2
        self.repository.add_playlist_song(playlist_song1)
        self.repository.add_playlist_song(playlist_song2)
        songs = self.repository.get_songs_by_playlist_id(1)  # Assuming playlist_id is 1
        self.assertEqual(len(songs), 2)
        self.assertIn(1, songs)  # Assuming song_id is 1
        self.assertIn(2, songs)  # Assuming song_id is 2

    def test_get_playlist_ids_by_song_id(self):
        playlist_song1 = PlaylistSongs(1, 1)  # Assuming playlist_id and song_id are 1
        playlist_song2 = PlaylistSongs(2, 1)  # Assuming playlist_id is 2 and song_id is 1
        self.repository.add_playlist_song(playlist_song1)
        self.repository.add_playlist_song(playlist_song2)
        playlists = self.repository.get_playlist_ids_by_song_id(1)  # Assuming song_id is 1
        self.assertEqual(len(playlists), 2)
        self.assertIn(1, playlists)  # Assuming playlist_id is 1
        self.assertIn(2, playlists)  # Assuming playlist_id is 2

if __name__ == '__main__':
    unittest.main()
