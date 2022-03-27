from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


def draw_line(coords, color_index):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4,
                       joinstyle='round', capstyle='projecting')


def draw_corner(args, color, isY=True):
    '''Actions 0xF4 (Y-corner) and 0xF5 (X-corner)'''
    x, y = args[0], args[1]
    coords = [(x, y)]
    for i in range(2, len(args)):
        x, y = (x, args[i]) if isY else (args[i], y)
        isY = not isY
        coords.append((x, y))
    draw_line(coords, color)


def draw_abs(args, color):
    '''Action 0xF6 (Absolute line)'''
    coords = [(args[0], args[1])]
    for i in range(2, len(args), 2):
        coords.append((args[i], args[i + 1]))
    draw_line(coords, color)


def draw_rel(args, color):
    '''Action 0xF7 (Relative line)'''
    x, y = args[0], args[1]
    coords = [(x, y)]
    for i in range(2, len(args)):
        xd, yd = args[i] >> 4 & 7, args[i] & 7
        xs, ys = args[i] >> 4 & 8, args[i] & 8
        x += -xd if xs else xd
        y += -yd if ys else yd
        coords.append((x, y))
    coords += coords if len(coords) == 1 else []
    draw_line(coords, color)


def log(pic):
    # Parse commands from file
    commands = []
    index = -1
    for byte in pic:
        if byte >= 0xf0:
            commands.append([])
            index += 1
        commands[index].append(byte)

    log = open('draw.log', 'w')

    # Action (logging) loop
    for cmd in commands:
        argprint = True
        action, args = cmd[0], cmd[1:]
        argstr = [f'{num:02X}' for num in args]
        argstr = ", ".join(argstr) if len(argstr) else "None"
        match action:
            case 0xf0:
                log.write(f'F0: Enabled picture draw\n')
            case 0xf1:
                log.write(f'F1: Disable picture draw\n')
            case 0xf2:
                log.write(f'F2: Enabled priority draw\n')
            case 0xf3:
                log.write(f'F3: Disable priority draw\n')
            case 0xf4:
                log.write(f'F4: Draw Y corner\n')
            case 0xf5:
                log.write(f'F5: Draw X corner\n')
            case 0xf6:
                log.write(f'F6: Absolute line\n')
            case 0xf7:
                log.write(f'F7: Relative line\n')
            case 0xf8:
                log.write(f'F8: Fill\n')
            case 0xf9:  # not used in given pictures
                log.write(f'F9: Pen size and style\n')
            case 0xfa:  # not used in given pictures
                log.write(f'FA: Plot with pen\n')
            case 0xff:
                log.write(f'FF: End of file\n')
        log.write(f'\tArguments: {argstr}\n')


def draw(pic):
    # Parse commands from file
    commands = []
    index = -1
    for byte in pic:
        if byte >= 0xf0:
            commands.append([])
            index += 1
        commands[index].append(byte)

    # Picture screen variables
    piccolor = None
    picdraw = None

    # Action loop
    for cmd in commands:
        action, args = cmd[0], cmd[1:]
        if action == 0xf0:
            picdraw = True
            piccolor = args[0]
        if action == 0xf1:
            picdraw = False
        if action == 0xf4 and picdraw:
            draw_corner(args, piccolor, isY=True)
        if action == 0xf5 and picdraw:
            draw_corner(args, piccolor, isY=False)
        if action == 0xf6 and picdraw:
            draw_abs(args, piccolor)
        if action == 0xf7 and picdraw:
            draw_rel(args, piccolor)


pic = Path('practice4\data\PIC.1').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()
