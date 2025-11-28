import heapq

# Generate next valid states

def get_neighbors(state):
    """
    Given a state = (pegA, pegB, pegC),
    each peg is a tuple of disks with the TOP at the RIGHT.
    Example: ((3,2,1), (), ()) means all 3 disks on peg A.
    """
    neighbors = []
    pegs = list(state)

    for i in range(3):  # from peg i
        if not pegs[i]:
            continue

        disk = pegs[i][-1]  # top disk of peg i

        for j in range(3):  # to peg j
            if i == j:
                continue

            # valid move if destination peg is empty
            # or its top disk is larger than the moving disk
            if (not pegs[j]) or pegs[j][-1] > disk:
                new_pegs = [list(p) for p in pegs]
                new_pegs[i].pop()
                new_pegs[j].append(disk)
                neighbors.append(tuple(tuple(p) for p in new_pegs))

    return neighbors

# Heuristic for A*

def heuristic(state, goal_peg_index=2):
    """
    Simple admissible heuristic:
    h(n) = number of disks NOT on the goal peg.
    Each such disk must move at least once, so h never overestimates.
    """
    h = 0
    for peg_index, peg in enumerate(state):
        if peg_index != goal_peg_index:
            h += len(peg)
    return h

# A* Search

def astar(start, goal):
    goal_peg_index = 2  # goal: all disks on third peg (index 2)

    # priority queue entries: (f, g, state, path)
    open_list = []
    g_start = 0
    h_start = heuristic(start, goal_peg_index)
    heapq.heappush(open_list, (g_start + h_start, g_start, start, [start]))

    # best known cost g(n) for each state
    best_g = {start: 0}

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        # goal test
        if state == goal:
            return path

        # if we already found a better way to this state, skip
        if g > best_g[state]:
            continue

        for nbr in get_neighbors(state):
            new_g = g + 1  # cost per move = 1

            if nbr not in best_g or new_g < best_g[nbr]:
                best_g[nbr] = new_g
                new_f = new_g + heuristic(nbr, goal_peg_index)
                heapq.heappush(open_list, (new_f, new_g, nbr, path + [nbr]))

    return None  # no path found (shouldn't happen for this problem)


# MAIN

if __name__ == "__main__":
    # 3 disks: 3 = biggest, 1 = smallest
    start_state = ((3, 2, 1), (), ())   # all disks on peg A
    goal_state  = ((), (), (3, 2, 1))   # goal: all disks on peg C

    astar_path = astar(start_state, goal_state)

    print("=========== A* SEARCH ===========")
    print("Moves:", len(astar_path) - 1)
    print("Path (states):")
    for state in astar_path:
        print(state)
