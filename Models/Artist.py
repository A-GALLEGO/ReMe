import uuid

class Artist:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id if id is not None else str(uuid.uuid4())


    @staticmethod
    def init_from_db_row(row):
        return Artist(row[1], row[0])

    def __str__(self):
        return f"Artist ID: {self.id}, Name: {self.name}"

