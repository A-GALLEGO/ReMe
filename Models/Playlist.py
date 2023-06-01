import uuid

class Playlists:
    def __init__(self, id=None, name=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name

    def __str__(self):
        return f"Playlist ID: {self.id}, Name: {self.name}"
