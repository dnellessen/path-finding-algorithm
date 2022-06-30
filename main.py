import pygame
import numpy as np
import time


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (150, 0, 0)
    green = (0, 150, 0)
    blue = (0, 50, 150)

    gray20 = (20, 20, 20)
    gray25 = (25, 25, 25)
    gray200 = (200, 200, 200)


class Grid:
    grid = [[0 for c in range(43)] for r in range(24)]
    start = None
    end = None

    @staticmethod
    def reset():
        '''Resets grid by filling array with zeros.'''

        Grid.grid = [[0 for c in range(43)] for r in range(24)]

    @staticmethod
    def update(coords=None, value=None):
        '''Updates grid by drawing rectagles on screen.'''

        if coords:
            row, col = coords
            Grid.grid[row][col] = value
            rect = pygame.Rect(
                (GUI.square.margin + GUI.square.width) *
                col + GUI.square.margin + 4,
                (GUI.square.margin + GUI.square.height) *
                row + GUI.square.margin + 40,
                GUI.square.width,
                GUI.square.height
            )
            pygame.draw.rect(GUI.screen, GUI.pen.color(value), rect)
        else:
            for row in range(24):
                for col in range(43):
                    rect = pygame.Rect(
                        (GUI.square.margin + GUI.square.width) *
                        col + GUI.square.margin + 4,
                        (GUI.square.margin + GUI.square.height) *
                        row + GUI.square.margin + 40,
                        GUI.square.width,
                        GUI.square.height
                    )
                    pygame.draw.rect(GUI.screen, GUI.pen.color(
                        Grid.grid[row][col]), rect)

        pygame.display.update()

    @staticmethod
    def template():
        '''Updates grid to template.'''

        Grid.grid = [
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0],
            [0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0],
            [0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0],
            [0, 3, 3, 3, 0, 3, 0, 3, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 3, 0],
            [0, 0, 3, 0, 0, 3, 0, 3, 0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 3, 0, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 3, 3, 0],
            [0, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0],
            [0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0],
            [3, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 0, 0, 3, 0],
            [0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0],
            [0, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 3, 0],
            [0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0],
            [3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3],
            [0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 3],
            [0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0],
            [0, 0, 3, 0, 3, 0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0],
            [0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 3, 0, 0, 3],
            [0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]]
        Grid.start = None
        Grid.end = None
        Grid.update()


class GUI:
    width, height = (1000, 600)
    fps = 60
    running = True

    pygame.init()
    pygame.display.set_caption('Path Finding Algorithm')
    screen = pygame.display.set_mode((width, height))
    screen.fill(Colors.gray25)

    font = pygame.font.SysFont('Arial', 20)

    mousepressed = False
    allowinput = True
    error = None

    class square:
        width, height = 20, 20
        margin = 3

    class pen:
        current = 1

        fill = 0
        start = 1
        end = 2
        barrier = 3
        path = 4
        visualize = 5

        colors = {
            0: Colors.gray20,
            1: Colors.green,
            2: Colors.red,
            3: Colors.gray200,
            4: Colors.blue,
            5: Colors.black,
        }

        values = {
            0: 'Remove',
            1: 'Start',
            2: 'End',
            3: 'Barrier',
        }

        @classmethod
        def color(cls, value) -> tuple:
            return cls.colors.get(value)

    def reset(self):
        '''Resets values and grid.'''

        if not GUI.allowinput:
            for r in range(24):
                for c in range(43):
                    if Grid.grid[r][c] == GUI.pen.path or Grid.grid[r][c] == GUI.pen.visualize:
                        Grid.grid[r][c] = 0
        else:
            if Grid.start and Grid.end:
                sr, sc = Grid.start
                er, ec = Grid.end
                Grid.grid[sr][sc] = 0
                Grid.grid[er][ec] = 0
            else:
                Grid.reset()
            Grid.start = None
            Grid.end = None
            GUI.pen.current = GUI.pen.start
        GUI.mousepressed = False
        GUI.allowinput = True

    def quit(self):
        pygame.quit()

    def run(self):
        '''Main run loop of screen.'''

        clock = pygame.time.Clock()
        while self.running:
            clock.tick(GUI.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if GUI.allowinput:
                    if event.type == pygame.MOUSEBUTTONDOWN or GUI.mousepressed:
                        x, y = pygame.mouse.get_pos()
                        if y > 50:
                            GUI.mousepressed = True
                            row = y // (GUI.square.height +
                                        GUI.square.margin) - 2
                            col = x // (GUI.square.width + GUI.square.margin)

                            try:
                                Grid.grid[row][col] = GUI.pen.current
                            except IndexError:
                                pass
                            else:
                                if GUI.pen.current == GUI.pen.fill or GUI.pen.current == GUI.pen.barrier:
                                    if (row, col) == Grid.start:
                                        Grid.start = None
                                    if (row, col) == Grid.end:
                                        Grid.end = None
                                elif GUI.pen.current == GUI.pen.start and not Grid.start:
                                    Grid.start = (row, col)
                                    Grid.end = None if Grid.start == Grid.end else Grid.end
                                    GUI.pen.current = GUI.pen.end if not Grid.end else GUI.pen.barrier
                                    GUI.mousepressed = False
                                elif GUI.pen.current == GUI.pen.end and not Grid.end:
                                    Grid.end = (row, col)
                                    Grid.start = None if Grid.end == Grid.start else Grid.start
                                    GUI.pen.current = GUI.pen.start if not Grid.start else GUI.pen.barrier
                                    GUI.mousepressed = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        GUI.mousepressed = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            if not Grid.start:
                                GUI.pen.current = GUI.pen.start
                            else:
                                GUI.pen.current = GUI.pen.barrier
                        if event.key == pygame.K_e and not Grid.end:
                            if not Grid.end:
                                GUI.pen.current = GUI.pen.end
                            else:
                                GUI.pen.current = GUI.pen.barrier
                        if event.key == pygame.K_b:
                            GUI.pen.current = GUI.pen.barrier
                        if event.key == pygame.K_r:
                            GUI.pen.current = GUI.pen.fill
                        if event.key == pygame.K_v:
                            Algorithm.visualize = False if Algorithm.visualize else True
                        if event.key == pygame.K_d:
                            Algorithm.diagonal = False if Algorithm.diagonal else True
                        if event.key == pygame.K_t:
                            Grid.template()
                        if event.key == pygame.K_SPACE and GUI.allowinput:
                            if not Grid.start:
                                GUI.error = {
                                    'message': 'No start set',
                                    'expires': time.time() + 2,
                                }
                                GUI.pen.current = GUI.pen.start
                            elif not Grid.end:
                                GUI.error = {
                                    'message': 'No end set',
                                    'expires': time.time() + 2,
                                }
                                GUI.pen.current = GUI.pen.end
                            else:
                                succeeded = Algorithm(
                                    Grid.start, Grid.end).run()
                                if not succeeded:
                                    GUI.error = {
                                        'message': 'Cannot be solved',
                                        'expires': time.time() + 2,
                                    }
                                    GUI.pen.current = GUI.pen.fill
                                else:
                                    GUI.allowinput = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.reset()
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            GUI.screen.fill(Colors.gray25)
            GUI.screen.blit(GUI.font.render(
                f'Visualize:  {Algorithm.visualize}', True, Colors.gray200), (325, 10))
            GUI.screen.blit(GUI.font.render(
                f'Diagonal:  {Algorithm.diagonal}', True, Colors.gray200), (525, 10))

            current = GUI.pen.current
            value = GUI.pen.values[current]
            color = Colors.white if value == 'Remove' else GUI.pen.color(
                current)
            GUI.screen.blit(GUI.font.render(value, True, color), (10, 10))

            if GUI.error:
                GUI.screen.blit(GUI.font.render(
                    GUI.error['message'], True, Colors.red), (GUI.width - len(GUI.error['message'])*10-10, 10))
                if GUI.error['expires'] < time.time():
                    GUI.error = None
                    for r in range(24):
                        for c in range(43):
                            if Grid.grid[r][c] == GUI.pen.visualize:
                                Grid.grid[r][c] = 0

            Grid.update()

        self.quit()


class Algorithm:
    diagonal = False
    visualize = False

    def __init__(self, start, end):
        '''
        Find the shortest and best path between two given points a given grid.
        The grid must have a start and end point.
        '''

        self.path = []

        shape = np.shape(Grid.grid)
        self.sr, self.sc = shape[0] - 1, shape[1] - 1

        self.start = start
        self.end = end

        self.finished = False
        self.runnable = True if self.start and self.end else False

    def run(self) -> bool:
        '''Runs algorithm and returns False if grid could not be solved.'''

        if not self.runnable and self.finished:
            return False
        res = self._breadthfirstsearch()
        if not res:
            return False
        self._reconstruct_path(res)
        self._update_grid()
        return True

    def _breadthfirstsearch(self) -> dict:
        '''
        Breadth-first search (BFS) algorithm
        Returns a dictionary with parents as keys with every child as values.
        '''

        result = {}
        visited = []
        queue = []

        queue.append(self.start)
        visited.append(self.start)

        while queue and not self.finished:
            v = queue.pop(0)

            for n in self._neighbors(v):
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

                    if self.visualize and n != self.end:
                        Grid.update(n, GUI.pen.visualize)

                    try:
                        result[v].append(n)
                    except KeyError:
                        result[v] = [n]

            if len(queue) == 0:
                return None

        return result

    def _neighbors(self, position: tuple):
        '''Yields all possible neighbors of a given position.'''

        r, c = position

        if self.diagonal:
            possible = [
                (r+1, c),    # north
                (r, c+1),    # east
                (r-1, c),    # south
                (r, c-1),    # west
                (r+1, c+1),  # northeast
                (r-1, c+1),  # southeast
                (r-1, c-1),  # southwest
                (r+1, c-1),  # northwest
            ]
        else:
            possible = [
                (r+1, c),  # north
                (r, c+1),  # east
                (r-1, c),  # south
                (r, c-1),  # west
            ]

        for n in possible:
            nr, nc = n
            if 0 <= nr <= self.sr and 0 <= nc <= self.sc:
                if Grid.grid[nr][nc] != GUI.pen.barrier:
                    yield n
                if n == self.end:
                    self.finished = True

    def _reconstruct_path(self, bfs_result: dict) -> list:
        '''Completes path by backtracking to every parent of position - starting at the end - and inserting that parent to a list.'''

        self.path.append(self.end)
        parent = self.end

        while parent != self.start:
            for p, c in bfs_result.items():
                if parent in c:
                    self.path.append(p)
                    parent = p

        self.path.reverse()
        return self.path

    def _update_grid(self) -> None:
        '''Updates grid by inserting symbol at path's positions.'''

        for position in self.path[1:-1]:
            Grid.update(position, GUI.pen.path)


if __name__ == '__main__':
    gui = GUI()
    gui.run()

    '''
    mouse click and drag   ->  draw tile

    s   ->  start tile
    e   ->  end tile
    b   ->  barrier tile
    r   ->  remove tile

    v   ->  switch visualize bool
    d   ->  switch diagonal bool

    t   ->  use grid template
    c   ->  clear gird (1 -> path and vis ; 2 -> start and end ; 3 -> all)

    space   ->  start
    '''

    
