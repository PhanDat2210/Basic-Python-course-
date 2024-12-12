import curses

# Mê cung Pac-Man
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

player_pos = [1, 1]  # Vị trí Pac-Man ban đầu


def draw_maze(stdscr, maze, player_pos):
    """Vẽ mê cung và vị trí Pac-Man."""
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                stdscr.addch(y, x, '#')  # Vẽ tường
            elif cell == 0:
                stdscr.addch(y, x, ' ')  # Không gian trống
            elif [y, x] == player_pos:
                stdscr.addch(y, x, 'P')  # Pac-Man


def main(stdscr):
    """Hàm chính xử lý di chuyển Pac-Man."""
    global player_pos
    curses.curs_set(0)  # Ẩn con trỏ
    stdscr.clear()
    draw_maze(stdscr, maze, player_pos)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        new_pos = player_pos[:]
        if key == curses.KEY_UP:
            new_pos[0] -= 1
        elif key == curses.KEY_DOWN:
            new_pos[0] += 1
        elif key == curses.KEY_LEFT:
            new_pos[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_pos[1] += 1

        # Kiểm tra tính hợp lệ của vị trí mới
        if maze[new_pos[0]][new_pos[1]] != 1:
            player_pos = new_pos

        stdscr.clear()
        draw_maze(stdscr, maze, player_pos)
        stdscr.refresh()


curses.wrapper(main)
