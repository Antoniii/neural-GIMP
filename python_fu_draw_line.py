# C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

# -*- coding: utf-8 -*-

import pdb
from gimpfu import *


def draw_line(image, layer, x1, y1, x2, y2, brush_size):
    image.undo_group_start()
    pdb.gimp_context_set_foreground((255, 165, 0))
    points = [(x1, y1), (x2, y2)]
    pdb.gimp_context_set_brush_size(brush_size) # установка размера кисти
    pdb.gimp_pencil(layer, len(points), [p for point in points for p in point])
    image.undo_group_end()
    gimp.displays_flush()

# зарегистрируйте функцию в GIMP
register(
    "python_fu_draw_line",
    "Draws an orange line on the active layer",
    "Draws an orange line on the active layer",
    "Author Name",
    "Author Name",
    "2023",
    "<Image>/Filters/Draw Line...",
    "*",
    [
        (PF_INT, "x1", "X-coordinate of start point", 10),
        (PF_INT, "y1", "Y-coordinate of start point", 10),
        (PF_INT, "x2", "X-coordinate of end point", 1250),
        (PF_INT, "y2", "Y-coordinate of end point", 1250),
        (PF_INT, "brush_size", "Brush size", 500)
    ],
    [],
    draw_line)

# запустите GIMP
main()