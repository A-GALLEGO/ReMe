import unittest
import tempfile
import os
from Repositories.SongRepository import SongRepository
from Models.Song import Songs

class SongRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mktemp()  # Create a temporary database file
        self.repository = SongRepository(self.db_file)
        self.repository.create_table()

    def tearDown(self):
        self.repository.disconnect()
        os.remove(self.db_file)

    def test_add_song(self):
        song = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song.mp3')
        self.repository.add_song(song)
        song_in_db = self.repository.get_song_by_id(song.id)
        self.assertEqual(song_in_db.id, song.id)
        self.assertEqual(song_in_db.name, song.name)
        self.assertEqual(song_in_db.idArtist, song.idArtist)
        self.assertEqual(song_in_db.duration, song.duration)
        self.assertEqual(song_in_db.filePath, song.filePath)

    def test_get_all_songs(self):
        song1 = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song1.mp3')
        song2 = Songs('Song 2', 'Artist 2', '4:15', '/path/to/song2.mp3')
        self.repository.add_song(song1)
        self.repository.add_song(song2)
        songs = self.repository.get_all_songs()
        self.assertGreaterEqual(len(songs), 2)

    def test_get_song_by_id(self):
        song = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song.mp3')
        self.repository.add_song(song)
        retrieved_song = self.repository.get_song_by_id(song.id)
        self.assertEqual(retrieved_song.name, song.name)
        self.assertEqual(retrieved_song.idArtist, song.idArtist)
        self.assertEqual(retrieved_song.duration, song.duration)
        self.assertEqual(retrieved_song.filePath, song.filePath)

    def test_get_song_path_by_id(self):
        song = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song.mp3')
        self.repository.add_song(song)
        retrieved_song = self.repository.get_song_path_by_id(song.id)
        self.assertEqual(retrieved_song.filePath, song.filePath)
     

    def test_update_song(self):
        song = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song.mp3')
        self.repository.add_song(song)
        song.name = "New name"
        song.duration = '4:00'
        song.filePath = '/path/to/new_song.mp3'
        self.repository.update_song(song)
        retrieved_song = self.repository.get_song_by_id(song.id)
        self.assertEqual(retrieved_song.name, song.name)
        self.assertEqual(retrieved_song.duration, song.duration)
        self.assertEqual(retrieved_song.filePath, song.filePath)

    def test_delete_song(self):
        song = Songs('Song 1', 'Artist 1', '3:30', '/path/to/song.mp3')
        self.repository.add_song(song)
        self.repository.delete_song(song.id)
        retrieved_song = self.repository.get_song_by_id(song.id)
        self.assertIsNone(retrieved_song)
    
    

if __name__ == '__main__':
    unittest.main()
