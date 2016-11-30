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
        new_darkness = abs(darkness-color.y)
        return COLOR.grid[new_x][new_darkness]

    def color_byname(name):
        for supercolor in COLOR.grid:
            for color in supercolor:
                if color.name == name:
                    return color
        return None


class Opcode:

    def __init__(self, token, shift_hue, shift_darkness):
        self.token = token
        self.shift_hue = shift_hue
        self.shift_darkness = shift_darkness

    def __equ__(self, token):
        return self.token == token

    def delta_color(self, current_color):
        return COLOR.shift_color(current_color, self.shift_hue, self.shift_darkness)


def main():
    COLOR.create_grid()
    code = input("CODE: ")
    if
    color_option = None
    starting_color = None
    while starting_color is None:
        color_option = input("Starting Color (h for help): ")
        if color_option == "h":
            strbuild = ""
            for supercolor in COLOR.grid:
                for color in supercolor:
                    strbuild += color.name + ";"
            print("Possible colors: "+strbuild)
        else:
            starting_color = COLOR.color_byname(color_option)
            if starting_color is None:
                print("Invalid color")


    compile("in(number)-duplicate-mul-out(number)",2,2)


def create_opcode_table():
    op_list = set()
    op_list.add(Opcode("push",0,1))
    op_list.add(Opcode("pop",0,2))
    op_list.add(Opcode("add",1,0))
    op_list.add(Opcode("sub",1,1))
    op_list.add(Opcode("mul",1,2))
    op_list.add(Opcode("div",2,0))
    op_list.add(Opcode("mod",2,1))
    op_list.add(Opcode("not",2,2))
    op_list.add(Opcode("greater",3,0))
    op_list.add(Opcode("pointer",3,1))
    op_list.add(Opcode("switch",3,2))
    op_list.add(Opcode("duplicate",4,0))
    op_list.add(Opcode("roll",4,1))
    op_list.add(Opcode("in(number)",4,2))
    op_list.add(Opcode("in(char)",5,0))
    op_list.add(Opcode("out(number)",5,1))
    op_list.add(Opcode("out(char)",5,2))
    return op_list


def compile(inputstring, startx=0, starty=0):
    opcodes = create_opcode_table()
    proc = inputstring.split("-")
    currentcolor = COLOR.get_color(startx, starty)
    color_list = [currentcolor]

    for str in proc:
        ok = False
        for opcode in opcodes:
            if opcode.token == str:
                currentcolor = opcode.delta_color(currentcolor)
                color_list.append(currentcolor)
                ok = True
                break
        if not ok:
            print("ERROR: "+str+" is an invalid opcode!")
            break

    for color in color_list:
        print(color.name)

main()