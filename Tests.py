
import sys
sys.path.append('../')

import unittest
from Tests.ArtistTests import ArtistRepositoryTests
from Tests.PlaylistTest import PlaylistRepositoryTests
from Tests.SongTests import SongRepositoryTests
from Tests.PlaylistSongTest import PlaylistSongsRepositoryTests


if __name__ == '__main__':
    unittest.main()
    