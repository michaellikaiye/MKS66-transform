# MKS66-transform
##Does the following:
- create a translation matrix
- create a scale matrix
- create a rotation matrix about the x-axis
- create a rotation matrix about the y-axis
- create a rotation matrix about the z-axis

##Main routine keeps track of:
A single edge matrix
A single master transformation matrix

##Creates a parser that will interpret a script to be used to draw an image.
Each command is a single word without spaces in it, and if it takes arguments, the line after will contain the arguments, separated by spaces.

##Full list of commands:
line: add a line to the point matrix -  takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
ident: set the transform matrix to the identity matrix
scale: create a scale matrix, then multiply the transform matrix by the scale matrix -  takes 3 arguments (sx, sy, sz)
move: create a translation matrix, then multiply the transform matrix by the translation matrix - takes 3 arguments (tx, ty, tz)
rotate: create a rotation matrix, then multiply the transform matrix by the rotation matrix - takes 2 arguments (axis theta)
apply: apply the current transformation matrix to the edge matrix
display: clear the screen, draw the lines of the point matrix to the screen, display the screen
save: clear the screen, draw the lines of the point matrix to the screen/frame save the screen/frame to a file - takes 1 argument (file name)\
