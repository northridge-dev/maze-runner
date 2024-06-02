import subprocess
import sys

from maze import Maze

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python maze.py {bfs|dps} maze001")

    m = Maze(sys.argv[1], sys.argv[2])
    print("Maze:")
    m.print()
    print("Solving...")
    m.solve()
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image("maze.png", show_explored=True)
    subprocess.run(["open", "maze.png"])
