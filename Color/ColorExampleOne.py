class ColorExampleOne:
    category: str = 'painting'

    def __init__(self, player_id: int, name: str, red: int, green: int, blue: int):
        self.player_id: int = player_id
        self.name: str = name
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.complementary_colors = []  # proper usage of instance variable

    def paint_wall(self):
        print("Wall painted {0}".format(self.name))


if __name__ == '__main__':
    color_1 = ColorExampleOne(1, 'purple', 0, 100, 150)
    color_1.complementary_colors.append('red')    # add comp. colors to first instance
    color_1.complementary_colors.append('blue')  # add comp. colors to first instance
    print(color_1.complementary_colors)

    color_2 = ColorExampleOne(2, 'red', 255, 0, 0)
    color_2.complementary_colors.append('purple')   # change in instance variable
    print(color_1.complementary_colors)    # no impact on another instance
    print(color_2.complementary_colors)    # only changed appropriate instance variable
