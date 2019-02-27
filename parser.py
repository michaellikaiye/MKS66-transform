from display import *
from matrix import *
from draw import *

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
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    lines = f.read().split('\n')
    n = 0
    while n < len(lines):
        print(n+1)
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

        print_matrix(points)
