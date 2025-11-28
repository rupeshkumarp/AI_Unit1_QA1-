
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

            # valid move: j empty OR top disk larger than moving disk
            if (not pegs[j]) or pegs[j][-1] > disk:
                new_pegs = [list(p) for p in pegs]
                new_pegs[i].pop()
                new_pegs[j].append(disk)
                neighbors.append(tuple(tuple(p) for p in new_pegs))

    return neighbors



# DFS Search

def dfs(start, goal):
    stack = [(start, [start])]
    visited = {start}

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                stack.append((nxt, path + [nxt]))

    return None

# MAIN

start_state = ((3, 2, 1), (), ())    # all disks on peg A
goal_state  = ((), (), (3, 2, 1))    # all disks on peg C

dfs_path = dfs(start_state, goal_state)

print("=========== DFS SEARCH ===========")
print("Moves:", len(dfs_path) - 1)
print("Path:")
for state in dfs_path:
    print(state)
