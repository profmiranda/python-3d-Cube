class Color:
    category: str = 'painting'

    def __init__(self, player_id: int, name: str, red: int, green: int, blue: int):
        self.player_id: int = player_id
        self.name: str = name
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.data: list = []  # extra

    def paint_wall(self):
        print("Wall painted {0}".format(self.name))


if __name__ == '__main__':
    color_1 = Color(1, 'purple', 0, 100, 150)
    color_2 = Color(2, 'red', 255, 0, 0)

    print(color_1.player_id)
    print(color_2.player_id)

    print(color_1.category)
    print(color_2.category)
