import uuid

class Songs:
    def __init__(self, id=None, name=None, idArtist=None, duration=None, filePath=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.idArtist = idArtist
        self.duration = duration
        self.filePath = filePath

    def __str__(self):
        return f"Song ID: {self.id}, Name: {self.name}, Artist ID: {self.idArtist}, Duration: {self.duration}, FilePath: {self.filePath}"
