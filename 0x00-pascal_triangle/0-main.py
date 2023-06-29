#!/usr/bin/python3

from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

triangle = pascal_triangle(5)
print_triangle(triangle)

