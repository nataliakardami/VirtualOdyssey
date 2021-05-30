# http://programarcadegames.com/index.php?chapter=lab_adventure
# http://programarcadegames.com/index.php?chapter=lab_final

class Character(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        """
        String representation of character's name
        :return:
        """
        return str(self.name)

    def get_name(self) -> object:
        return self.name

    def get_character_desc(self):
        return self.description

    def print_character_desc(self):
        print(self.description)


class Player(Character):
    def __init__(self, description):
        # super().__init__(name = self.set_name(self))
        self.set_name()
        self.bag = []
        self.description = description
        self.morality_score = 0

    def set_name(self):
        name = "What is your name? "
        self.name = input(name)

    def change_morality_score(self, score):
        self.morality_score += score

    def get_morality_score(self):
        return self.morality_score


class NonPlayableCharacter(Character):
    def __init__(self):
        super(NonPlayableCharacter, self).__init__()

    def ally_or_enemy(self, is_ally):
        """

        :type is_ally: bool
        """
        if is_ally:
            return self.name + " is an ally."
        else:
            return self.name + " is an enemy."


class Collectables(object):

    def __init__(self, item_name, score):
        """
        :type item_name: str
        :type score: int
        """
        self.item_name = item_name
        self.score = score

    def __str__(self):
        return str(self.item_name, " is worth ", self.score)


if __name__ == '__main__':
    char = Character("name", "desc")
    print(char.name)
    player = Player("descr")
    player.print_character_desc()
