from enum import Enum


class TournamentType(Enum):
    QUALIFIER = 0
    FINAL = 1


class Tournament:
    def __init__(self, id, name, type, season, number):
        self.id = id
        self.name = name
        self.type = type
        self.season = season
        self.number = number
