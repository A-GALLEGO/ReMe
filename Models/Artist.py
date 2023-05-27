import uuid

class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Artist ID: {self.id}, Name: {self.name}"

