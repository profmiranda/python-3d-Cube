import random


class ColorDeprecated:
    randomInt = random.randint(0, 9999)

    def __init__(self, player_id: int, name: str, red: int, green: int, blue: int):
        self.player_id: int = player_id
        self.name: str = name
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.data: list = []  # extra
        # self.ex1: float = 2.4
        # self.ex2: bool = True
        # self.ex3: dict = {"x": "y"}
        # self.ex4: set = {"a", "b", "c"}
        # self.ex5: tuple = ("name", "age", "job")

    def paint_wall(self):
        print("Wall painted {0}".format(self.name))


if __name__ == '__main__':
    color_1 = ColorDeprecated(1, 'purple', 0, 100, 150)
    color_2 = ColorDeprecated(1, 'red', 255, 0, 0)
    color_1.paint_wall()
    color_2.paint_wall()

    color_1.new_attribute_str = 'thee'
    print(color_1.new_attribute_str)
    # print(color_2.new_attribute_str) - incorrect

    color_1.red = 230   # correct
    color_1.randomInt = random.randint(0, 9999)  # correct
    ColorDeprecated.randomInt = random.randint(0, 9999)   # correct

    color_1.paint_wall()    # correct
    ColorDeprecated.paint_wall(color_1)   # correct
    ColorDeprecated.paint_wall(color_2)   # correct
