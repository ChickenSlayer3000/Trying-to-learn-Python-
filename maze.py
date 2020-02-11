#!/usr/bin/env python
"""Random Maze Generator"""
from tkinter import Tk, Canvas
from random import randint

CELL_SIZE = 9  # pixels
MAZE_SIZE = 100  # rows and columns


def create(ffs, maze_map):
    """Check rows and columns and draw stuff"""
    for row in range(MAZE_SIZE):
        for col in range(MAZE_SIZE):
            if maze_map[row][col] == "P":
                color = "White"
            elif maze_map[row][col] == "w":
                color = "black"
            draw(ffs, row, col, color)


def draw(ffs, row, col, color):
    """Draw rectangles"""
    x_one = col * CELL_SIZE
    y_one = row * CELL_SIZE
    x_two = x_one + CELL_SIZE
    y_two = y_one + CELL_SIZE
    ffs.create_rectangle(x_one, y_one, x_two, y_two, fill=color)


def check_neighbours(ccr, ccc, maze_map):
    """This function checks neighbours"""
    walls = []
    neighbours = [
        [
            ccr,
            ccc - 1,
            ccr - 1,
            ccc - 2,
            ccr,
            ccc - 2,
            ccr + 1,
            ccc - 2,
            ccr - 1,
            ccc - 1,
            ccr + 1,
            ccc - 1,
        ],  # left
        [
            ccr,
            ccc + 1,
            ccr - 1,
            ccc + 2,
            ccr,
            ccc + 2,
            ccr + 1,
            ccc + 2,
            ccr - 1,
            ccc + 1,
            ccr + 1,
            ccc + 1,
        ],  # right
        [
            ccr - 1,
            ccc,
            ccr - 2,
            ccc - 1,
            ccr - 2,
            ccc,
            ccr - 2,
            ccc + 1,
            ccr - 1,
            ccc - 1,
            ccr - 1,
            ccc + 1,
        ],  # top
        [
            ccr + 1,
            ccc,
            ccr + 2,
            ccc - 1,
            ccr + 2,
            ccc,
            ccr + 2,
            ccc + 1,
            ccr + 1,
            ccc - 1,
            ccr + 1,
            ccc + 1,
        ],  # bottom
    ]
    visitable_neighbours = []
    for i in neighbours:  # find neighbours to visit
        if i[0] > 0 and i[0] < (MAZE_SIZE - 1) and i[1] > 0 and i[1] < (MAZE_SIZE - 1):
            if (
                maze_map[i[2]][i[3]] == "P"
                or maze_map[i[4]][i[5]] == "P"
                or maze_map[i[6]][i[7]] == "P"
                or maze_map[i[8]][i[9]] == "P"
                or maze_map[i[10]][i[11]] == "P"
            ):
                walls.append(i[0:2])
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_neighbours


def main():
    """Main"""
    maze_map = [["w" for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
    scr = randint(1, MAZE_SIZE)
    scc = randint(1, MAZE_SIZE)
    start_color = "Green"
    ccr, ccc = scr, scc

    maze_map[ccr][ccc] = "P"
    finished = False
    visited_cells = []
    revisited_cells = []
    while not finished:
        visitable_neighbours = check_neighbours(ccr, ccc, maze_map)
        if len(visitable_neighbours) != 0:
            d = randint(1, len(visitable_neighbours)) - 1
            ncr, ncc = visitable_neighbours[d]
            maze_map[ncr][ncc] = "P"
            visited_cells.append([ncr, ncc])
            ccr, ccc = ncr, ncc
        if len(visitable_neighbours) == 0:
            try:
                ccr, ccc = visited_cells.pop()
                revisited_cells.append([ccr, ccc])
            except:
                finished = True

    window = Tk()
    window.title("Maze")
    canvas_side = MAZE_SIZE * CELL_SIZE
    ffs = Canvas(window, width=canvas_side, height=canvas_side, bg="grey")
    ffs.pack()
    create(ffs, maze_map)
    draw(ffs, scr, scc, start_color)
    e = randint(1, len(revisited_cells)) - 1
    ecr = revisited_cells[e][0]
    ecc = revisited_cells[e][1]
    end_color = "red"
    draw(ffs, ecr, ecc, end_color)
    print(revisited_cells)
    window.mainloop()


if __name__ == "__main__":
    main()
