import unittest
import tempfile
import os
from Repositories.PlaylistRepository import PlaylistRepository
from Models.Playlist import Playlists

class PlaylistRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mktemp()  # Create a temporary database file
        self.repository = PlaylistRepository(self.db_file)
        self.repository.create_table()

    def tearDown(self):
        self.repository.disconnect()
        os.remove(self.db_file)

    def test_add_playlist(self):
        playlist = Playlists('Playlist 1')
        self.repository.add_playlist(playlist)
        playlist_in_db = self.repository.get_playlist_by_id(playlist.id)
        self.assertEqual(playlist_in_db.id, playlist.id)
        self.assertEqual(playlist_in_db.name, playlist.name)

    def test_get_all_playlists(self):
        playlist1 = Playlists('Playlist 1')
        playlist2 = Playlists('Playlist 2')
        self.repository.add_playlist(playlist1)
        self.repository.add_playlist(playlist2)
        playlists = self.repository.get_all_playlists()
        self.assertGreaterEqual(len(playlists), 2)

    def test_get_playlist_by_id(self):
        playlist = Playlists('Playlist 1')
        self.repository.add_playlist(playlist)
        retrieved_playlist = self.repository.get_playlist_by_id(playlist.id)
        self.assertEqual(retrieved_playlist.name, playlist.name)

    def test_update_playlist(self):
        playlist = Playlists('Playlist 1')
        self.repository.add_playlist(playlist)
        playlist.name = "New name"
        self.repository.update_playlist(playlist)
        retrieved_playlist = self.repository.get_playlist_by_id(playlist.id)
        self.assertEqual(retrieved_playlist.name, playlist.name)

    def test_delete_playlist(self):
        playlist = Playlists('Playlist 1')
        self.repository.add_playlist(playlist)
        self.repository.delete_playlist(playlist.id)
        retrieved_playlist = self.repository.get_playlist_by_id(playlist.id)
        self.assertIsNone(retrieved_playlist)

if __name__ == '__main__':
    unittest.main()
