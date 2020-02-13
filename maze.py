import tkinter, random, itertools
sq, rows = 9, range(100)  # cell size in pixels; sequence of row indices
color = dict(free='white', wall='black', start='green', end='red')
coord = lambda z: (int(z.real)*sq, -int(z.imag)*sq)  # complex to screen
rect = lambda *sides: {j-i*1j for i,j in itertools.product(*sides)}
pick = lambda iterable: random.choice(list(iterable))
maze, seen, reseen = dict.fromkeys(rect(rows,rows),'wall'), set(), set()
pos = pick(maze); maze[pos] = 'start'
while ...:
    ways = {d for d in (1,1j,-1,-1j) if all(maze.get(pos+d*t) == 'wall'
              for t in rect({-1,0,1}, {1,2}) - {1})}
    if ways:
        pos += pick(ways); seen.add(pos)
        if maze[pos] == 'wall': maze[pos] = 'free'
    elif seen: pos = seen.pop(); reseen.add(pos)
    else: break
maze[pick(reseen or seen)] = 'end'
window = tkinter.Tk(); window.title('Maze')
C = tkinter.Canvas(window, width=len(rows)*sq, height=len(rows)*sq)
for pos,cell in maze.items():
    C.create_rectangle(*coord(pos),*coord(pos + 1-1j), fill=color[cell])
C.pack();window.mainloop()
