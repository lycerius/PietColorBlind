class COLOR:
    grid = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    def __init__(self, name, x, y, hexi):
        self.x = x
        self.y = y
        self.name = name
        self.hexi = hexi

    def add_color(color):
        COLOR.grid[color.x][color.y] = color

    def create_grid():
        COLOR.add_color(COLOR("light red",0,0,"FFC0C0"))
        COLOR.add_color(COLOR("red", 0, 1, "FF0000"))
        COLOR.add_color(COLOR("dark red", 0, 2, "C00000"))

        COLOR.add_color(COLOR("light yellow", 1, 0, "FFFFC0"))
        COLOR.add_color(COLOR("yellow", 1, 1, "FFFF00"))
        COLOR.add_color(COLOR("dark yellow", 1, 2, "C0C000"))

        COLOR.add_color(COLOR("light green", 2, 0, "C0FFC0"))
        COLOR.add_color(COLOR("green", 2, 1, "00FF00"))
        COLOR.add_color(COLOR("dark green", 2, 2, "00C000"))

        COLOR.add_color(COLOR("light cyan", 3, 0, "C0FFFF"))
        COLOR.add_color(COLOR("cyan", 3, 1, "00FFFF"))
        COLOR.add_color(COLOR("dark cyan", 3, 2, "00C0C0"))

        COLOR.add_color(COLOR("light blue", 4, 0, "C0C0FF"))
        COLOR.add_color(COLOR("blue", 4, 1, "0000FF"))
        COLOR.add_color(COLOR("dark blue", 4, 2, "0000C0"))

        COLOR.add_color(COLOR("light magenta", 5, 0, "FFC0FF"))
        COLOR.add_color(COLOR("magenta", 5, 1, "FF00FF"))
        COLOR.add_color(COLOR("dark magenta", 5, 2, "C000C0"))
    def get_color(x,y):
        return COLOR.grid[x][y]

    def shift_color(color, hue, darkness):
        new_x = color.x
        for x in range(0,hue):
            new_x = (new_x + 1) % 6
        new_darkness = abs(color.y-darkness)
        return COLOR.grid[new_x][new_darkness]

def main():
    COLOR.create_grid()
    light_red = COLOR.get_color(0,0)
    print(light_red.name)
    new_color = COLOR.shift_color(light_red,1,0)
    print(new_color.name)
    new_new_color = COLOR.shift_color(new_color,6,0)
    print(new_new_color.name)
    create_plan("in(number)-in(number)")

def create_plan(inputstring, startx=0, starty=0):
    proc = inputstring.split("-")
    currentcolor = COLOR.get_color(startx, starty)
    color_list = [currentcolor]
    for str in proc:
        if str == "in(number)":
            currentcolor = COLOR.shift_color(currentcolor, 5, 0)
            color_list.append(currentcolor)
        else:
            print("Nope")
            break
    for color in color_list:
        print(color.name)

main()