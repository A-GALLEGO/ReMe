
import unittest
import tempfile
import os
from Repositories.ArtistRepository import ArtistRepository
from Models.Artist import Artist

class ArtistRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.mktemp()  # Create a temporary database file
        self.repository = ArtistRepository(self.db_file)
        self.repository.create_table()

    def tearDown(self):
        self.repository.disconnect()
        os.remove(self.db_file)

    def test_add_artist(self):
        artist = Artist('Artist 1')
        self.repository.add_artist(artist)
        artistInDb = self.repository.get_artist_by_id(artist.id)
        self.assertEqual(artistInDb.id, artist.id)
        self.assertEqual(artistInDb.name, artist.name)

    def test_get_all_artists(self):
        artist1 = Artist('Artist 1')
        artist2 = Artist('Artist 2')
        self.repository.add_artist(artist1)
        self.repository.add_artist(artist2)
        artists = self.repository.get_all_artists()
        self.assertGreaterEqual(len(artists), 2)

    def test_get_artist_by_id(self):
        artist = Artist('Artist 1')
        self.repository.add_artist(artist)
        retrieved_artist = self.repository.get_artist_by_id(artist.id)
        self.assertEqual(retrieved_artist.name, artist.name)

    def test_update_artist(self):
        artist = Artist('Artist 1')
        self.repository.add_artist(artist)
        artist.name = "New name"
        self.repository.update_artist(artist)
        retrieved_artist = self.repository.get_artist_by_id(artist.id)
        self.assertEqual(retrieved_artist.name, artist.name)

    def test_delete_artist(self):
        artist = Artist('Artist 1')
        self.repository.add_artist(artist)
        self.repository.delete_artist(artist.id)
        retrieved_artist = self.repository.get_artist_by_id(artist.id)
        self.assertIsNone(retrieved_artist)

if __name__ == '__main__':
    unittest.main()
