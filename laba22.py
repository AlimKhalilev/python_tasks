maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]

def LabExit(pos: (int, int), maze: list):
    lab = []
    for string in maze:
        lab.append(list(string))

    def get(pos: (int, int), lab: list):
       return lab[pos[1]][pos[0]]
    def set(pos: (int, int), lab: list, value):
       lab[pos[1]][pos[0]] = value

    exp1 = (pos[0] < 0 or pos[0] >= len(lab) or pos[1] < 0 or pos[1] >= len(lab[0]))
    exp2 = (get(pos, lab) == '#')

    if exp1 or exp2:
        print('Неверные координаты')
        return

    exits = []
    def SearchWays(pos: (int, int), lab: list):
        cell = get(pos, lab)
        if cell == '#':
            return
        if cell == ' ':
            newLab = lab.copy()
            set(pos, newLab, '#')
            SearchWays((pos[0] + 1, pos[1]), newLab)
            SearchWays((pos[0] - 1, pos[1]), newLab)
            SearchWays((pos[0], pos[1] + 1), newLab)
            SearchWays((pos[0], pos[1] - 1), newLab)
            return
        exits.append(cell)
    SearchWays(pos, lab)

    if len(exits) > 0:
        for i in exits:
            print(i, end=' ')
        print()
    else:
        print('Выхода нет')

inp = input("Введите координаты через пробел: ").split(' ')
LabExit((int(inp[0]), int(inp[1])), maze)