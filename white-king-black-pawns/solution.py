from collections import deque as Q

def nfr(f, r, i, j):
    files = "abcdefgh"
    _dir = {
        (1, 0): "R",
        (-1, 0): "L",
        (0, 1): "U",
        (0, -1): "D",
        (1, 1): "RU",
        (1, -1): "RD",
        (-1, 1): "LU",
        (-1, -1): "LD"
    }

    if (f == "a" and i < 0) or (f == "h" and i > 0):
        return (-1, -1)

    try:
        nf = files[files.index(f) + i]
    except IndexError:
        return (-1, -1)

    nr = int(r) + j
    if nr < 1 or nr > 8:
        return (-1, -1)

    return (nf + str(nr), _dir[(i, j)])

def get_next(pos):
    f, r = pos[0], pos[1]

    return [
        nfr(f, r, 1, 0),
        nfr(f, r, -1, 0),
        nfr(f, r, 0, 1),
        nfr(f, r, 0, -1),
        nfr(f, r, 1, 1),
        nfr(f, r, -1, -1),
        nfr(f, r, 1, -1),
        nfr(f, r, -1, 1),
    ]
def bfs(king_pos, pawns):
    q = Q()
    q.append((king_pos, []))
    vis = set()

    while len(q):
        pos, path = q.popleft()

        if pos[1] == "8":
            return "\n".join(path) + "\n#"

        if pos in vis: continue

        vis.add(pos)
        for next_pos, next_dir in get_next(pos):
            if next_pos != -1 and next_pos not in vis and next_pos not in pawns:
                q.append((next_pos, path + [next_dir]))
    return -1

king_pos, n = input().split()
pawns = input().split()

print(bfs(king_pos, pawns))
