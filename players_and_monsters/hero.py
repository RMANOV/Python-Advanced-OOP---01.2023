# Players and Monsters
# Your task is to create the following game hierarchy:
# 1. Hero : Elf, Wizard, Knight, MuseElf, DarkWizard, DarkKnight
#2. Elf : MuseElf
#3. Wizard : DarkWizard, SoulMaster
#4. Knight : DarkKnight, BladeKnight
# Create a class Hero. It should contain the following attributes:
# •	username: string
# •	level: int
# Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"

class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"

























