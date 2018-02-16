from enum import Enum


class Ethnic(Enum):
    HUMAN = {'hp': 300, 'mp': 300}
    ORC = {'hp': 400, 'mp': 200}
    ELF = {'hp': 250, 'mp': 400}


class Type(Enum):
    WARRIOR = {'attack': 80, 'long-attack': 40, 'defense': 30, 'spell': 30}
    WIZARD = {'attack': 20, 'long-attack': 60, 'defense': 20, 'spell': 80}
    ARCHER = {'attack': 40, 'long-attack': 80, 'defense': 20, 'spell': 40}


class Player:

    def __init__(self, name, type='WARRIOR', ethnic='HUMAN', lvl=1):
        self.name = name
        for typeValue in Type:
            if type == typeValue.name:
                self.type = typeValue
        for ethnicValue in Ethnic:
            if ethnic == ethnicValue.name:
                self.ethnic = ethnicValue
        self.level = lvl

    def __str__(self):
        return "Player "+self.name+" is a "+self.ethnic.name+" "+self.type.name






