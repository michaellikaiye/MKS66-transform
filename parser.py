from display import *
from matrix import *
from draw import *
import math
"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
0   1       2       3       4           5       6       7               8   9   10      11      12      13
Count,Name,Center X,Center Y,Center Z,Radius,Start Angle,Total Angle,End X,End Y,End Z,Start X,Start Y,Start Z
1,Line,,,,,,,207.0863,155.4836,1.8669,207.0863,155.4836,0.8914
1,Arc,207.0863,142.3145,1.8669,2.4387,180,90,,,,,,
"""
def add_arc(edge, radius, start, total, x, y, z):
    if z != 0.8914:
        points = []
        n = 6
        deg = start
        for i in range(n):
            inc = total/(n - 1)
            theta = math.radians(deg)
            ax = radius * math.cos(theta)
            ay = radius * math.sin(theta)
            incp = [x + ax, y + ay, z]
            points.append(incp)
            deg += inc
        for j in range(len(points) - 1):
            add_edge(edge, points[j][0],points[j][1], points[j][2], points[j+1][0], points[j+1][1], points[j+1][2])
        points = []
        n = 6
        deg = start
        for i in range(n):
            inc = total/(n - 1)
            theta = math.radians(deg)
            ax = radius * math.cos(theta)
            ay = radius * math.sin(theta)
            incp = [x + ax, y + ay, 0.8914]
            points.append(incp)
            deg += inc
        for j in range(len(points) - 1):
            add_edge(edge, points[j][0],points[j][1], points[j][2], points[j+1][0], points[j+1][1], points[j+1][2])

def parse_csv(fname, points, transform, screen, color):
    f = open(fname, 'r')
    lines = f.read().split('\n')
    n = 0
    while n < len(lines) - 1:
        words = lines[n].split(',')
        print(len(lines), n + 1)
        if words[1] == 'Line':
            ints = [float(words[8+x]) for x in range(6)]
            add_edge(points, ints[3], ints[4], ints[5], ints[0], ints[1], ints[2])
        if words[1] == 'Arc':
            ints = [float(words[2+x]) for x in range(6)]
            add_arc(points, ints[3], ints[4], ints[5], ints[0], ints[1], ints[2])
        n += 1
    ident(transform)
    x = make_rotX(30)
    matrix_mult(x, transform)
    y = make_rotY(30)
    matrix_mult(y, transform)
    z = make_rotX(30)
    matrix_mult(z, transform)
    matrix_mult(transform, points)
    clear_screen(screen)
    # draw_lines(points, screen, color)
    # display(screen)
    #


    ident(transform)
    t = make_translate(-100, -80, -100)
    matrix_mult(t, transform)
    s = make_scale(5, 5, 5)
    matrix_mult(s, transform)
    matrix_mult(transform, points)
    clear_screen(screen)
    draw_lines(points, screen, color)
    display(screen)
    save_extension(screen, 'key')

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    lines = f.read().split('\n')
    n = 0
    while n < len(lines):
        action = lines[n]
        if action == 'line':
            ints = [int(x) for x in lines[n+1].split(' ')]
            add_edge(points, ints[0], ints[1], ints[2], ints[3], ints[4], ints[5])
            n += 2
        elif action == 'ident':
            ident(transform)
            n += 1
        elif action == 'scale':
            ints = [int(x) for x in lines[n+1].split(' ')]
            s = make_scale(ints[0], ints[1], ints[2])
            matrix_mult(s, transform)
            n += 2
        elif action == 'move':
            ints = [int(x) for x in lines[n+1].split(' ')]
            t = make_translate(ints[0], ints[1], ints[2])
            matrix_mult(t, transform)
            n += 2
        elif action == 'rotate':
            axis = lines[n+1][0]
            words = lines[n+1].split(' ')
            if axis == 'x':
                r = make_rotX(int(words[1]))
            elif axis == 'y':
                r = make_rotY(int(words[1]))
            else:
                r = make_rotZ(int(words[1]))
            matrix_mult(r, transform)
            n += 2
        elif action == 'apply':
            matrix_mult(transform, points)
            #for i in len(points):
            #    for j in len(points[0]):
            #        points[i][j] = int(points[i][j])
            n += 1
        elif action == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            n += 1
        elif action == 'save':
            words = lines[n+1].split(' ')
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            save_extension(screen, words[0])
            n += 2
        elif action == 'quit':
            n = len(lines)
        else:
            n += 1
