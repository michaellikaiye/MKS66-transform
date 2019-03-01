from display import *
from draw import *
from parser import *
from matrix import *
# print("Testing MATRICES")
# print("Testing m2 = new_matrix(4,2)")
# m2 = []
# print("Testing add edge (1, 2, 3), (4, 5, 6)")
# add_edge(m2, 1, 2, 3, 4, 5, 6)
# print_matrix(m2)
# print("Testing identity matrix m0")
# m0 = new_matrix()
# ident(m0)
# print_matrix(m0)
# print("m1 =")
# m1 = []
# add_edge(m1, 1, 2, 3, 4, 5, 6)
# add_edge(m1, 7, 8, 9, 10, 11, 12)
# print_matrix(m1)
# print("Testing multiplication m1 * m2 =")
# matrix_mult(m1, m2)
# print_matrix(m2)
# print("Testing add point (1, 2, 3)")
# add_point(m2, 1, 2, 3)
# print_matrix(m2)

# s = make_scale(1,2,3)
# t = make_translate(4,5,6)
#
# print_matrix(s)
# print_matrix(t)
# s = [[2, 2, 2, 1]]
# matrix_mult(t, s)
#
# print_matrix(s)
#s = make_rotZ(60)
screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
parse_file( 'script', edges, transform, screen, color )
#parse_csv('Drawing2.csv', edges, transform, screen, color )
