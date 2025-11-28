from collections import deque

# Generate next valid states

def get_neighbors(state):
    neighbors = []
    pegs = list(state)

    for i in range(3):  # from peg i
        if not pegs[i]:
            continue

        disk = pegs[i][-1]  # top disk

        for j in range(3):  # to peg j
            if i == j:
                continue

            # Valid move: destination empty OR top disk larger
            if (not pegs[j]) or pegs[j][-1] > disk:
                new_pegs = [list(p) for p in pegs]
                new_pegs[i].pop()
                new_pegs[j].append(disk)
                neighbors.append(tuple(tuple(p) for p in new_pegs))

    return neighbors

# BFS Search

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path  # full path

        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None

# MAIN

start_state = ((3, 2, 1), (), ())     # all disks on peg A
goal_state  = ((), (), (3, 2, 1))     # goal: all disks to peg C

bfs_path = bfs(start_state, goal_state)

print("=========== BFS SEARCH ===========")
print("Moves:", len(bfs_path) - 1)
print("Path:")
for state in bfs_path:
    print(state)
