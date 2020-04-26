class Minimizer:
    def __init__(self, lst):
        self.lst = lst
        self.len = len(lst)
        self.tree = [range(0, self.len, 2)]
        l = len(self.tree[-1])
        while l > 1:
            self.tree.append([])
            for i in range(l / 2 + l % 2):
                self.tree[-1].append(self.tree[-2][2 * i])
            l = len(self.tree[-1])
    
    def _min(self, a, b):
        if self.lst[a][LEVEL] > self.lst[b][LEVEL]:
            return a
        if self.lst[a][LEVEL] < self.lst[b][LEVEL]:
            return b
        if self.lst[a][DISTANCE] is None:
            return b
        if self.lst[b][DISTANCE] is None:
            return a
        if self.lst[a][DISTANCE] <= self.lst[b][DISTANCE]:
            return a
        return b

    def update(self, a):
        if a % 2 == 0:
            idx0, idx1 = a, a + 1
        else:
            idx0, idx1 = a - 1, a
        up_idx = a / 2
        if idx1 < self.len:
            _m = self._min(idx0, idx1)
        else:
            _m = idx0
        if _m == self.tree[0][up_idx] and _m != a:
            return
        else:
            self.tree[0][up_idx] = _m
        level = 0
        level_idx = up_idx
        while level < len(self.tree) - 1:
            if level_idx % 2 == 0:
                idx0, idx1 = level_idx, level_idx + 1
            else:
                idx0, idx1 = level_idx - 1, level_idx
            up_idx = level_idx / 2
            if idx1 < len(self.tree[level]):
                _m = self._min(self.tree[level][idx0], self.tree[level][idx1])
            else:
                _m = self.tree[level][idx0]
            if _m == self.tree[level + 1][up_idx] and _m != a:
                break
            else:
                self.tree[level + 1][up_idx] = _m
            level += 1
            level_idx = up_idx

    def get(self):
        if len(self.tree[-1]) == 0:
            if len(self.lst) == 0:
                return None
            else:
                return 0
        else:
            return self.tree[-1][0]

class CMinimizer(Minimizer):
    '''We get a list of cities indices, _min is different...'''
    def _min(self, a, b):
        if cities[self.lst[a]][LEVEL] > cities[self.lst[b]][LEVEL]:
            return a
        if cities[self.lst[a]][LEVEL] < cities[self.lst[b]][LEVEL]:
            return b
        if cities[self.lst[a]][DISTANCE] is None:
            return b
        if cities[self.lst[b]][DISTANCE] is None:
            return a
        if cities[self.lst[a]][DISTANCE] <= cities[self.lst[b]][DISTANCE]:
            return a
        return b

class DMinimizer(Minimizer):
    def _min(self, a, b):
        if cities[self.lst[a]][LEVEL] > cities[self.lst[b]][LEVEL]:
            return a
        if cities[self.lst[a]][LEVEL] < cities[self.lst[b]][LEVEL]:
            return b
        if cities[self.lst[a]][DISTANCE] is None:
            return b
        if cities[self.lst[b]][DISTANCE] is None:
            return a
        if cities[self.lst[a]][DISTANCE] - cities[self.lst[a]][BESTDISTANCE] <= cities[self.lst[b]][DISTANCE] - cities[self.lst[b]][BESTDISTANCE]:
            return a
        return b

n, m = tuple(map(int, raw_input().split()))

LEVEL, DISTANCE, PARENT, BESTDISTANCE, BESTNEXT, INCITIESIDX, OUTCITIESIDX = 0, 1, 2, 3, 4, 5, 6
cities = []
for i in range(n):
    cities.append([0, None, None, None, None, None, None])
dijkstra_minimizer = Minimizer(cities)
matrix = []
roads = {}
for i in range(n):
    matrix.append({})
for i in range(m):
    u, v, w = tuple(map(int, raw_input().split()))
    if u > v:
        u, v = v, u
    roads[(u, v)] = None
    matrix[u][v] = w
    matrix[v][u] = w

# read more input
s, d = tuple(map(int, raw_input().split()))
q = int(raw_input())

cities[s] = [1, 0, None, None, None, None, None]
dijkstra_minimizer.update(s)

# Dijkstra to find initial best way
act = s
while act != d:
    for c in matrix[act]:
        new = cities[act][DISTANCE] + matrix[act][c]
        if (cities[c][DISTANCE] is None) or (cities[c][DISTANCE] > new):
            cities[c] = [1, new, act, None, None, None, None]
            dijkstra_minimizer.update(c)
    mn = dijkstra_minimizer.get()
    if cities[mn][DISTANCE] is None or cities[mn][LEVEL] == 0:
        break
    cities[mn][LEVEL] = 0
    dijkstra_minimizer.update(mn)
    act = mn

bestdistance = cities[d][DISTANCE]
if bestdistance is None:
    for i in range(q):
        raw_input()
        print 'Infinity'
    exit(0)

for r in roads:
    roads[r] = bestdistance

# update cities whith best way information
act = d
while 1:
    pt = cities[act][PARENT]
    cities[act] = [1, None, None, cities[act][DISTANCE], cities[act][BESTNEXT], None, None]
    if pt is None:
        break
    cities[pt][BESTNEXT] = act
    if act < pt:
        r = (act, pt)
    else:
        r = (pt, act)
    roads[r] = 'Infinity'
    act = pt
cities[s][LEVEL] = 0
cities[s][DISTANCE] = 0


# create minimizer lists
incities = []
outcities = []
incitiesidx = 0
outcitiesidx = 0
for idx, c in enumerate(cities):
    if c[BESTDISTANCE] is None:
        c[OUTCITIESIDX] = outcitiesidx
        outcitiesidx += 1
        outcities.append(idx)
        c[DISTANCE] = None
        c[LEVEL] = 0
    else:
        c[INCITIESIDX] = incitiesidx
        incitiesidx += 1
        incities.append(idx)

cmin = CMinimizer(outcities)
dmin = DMinimizer(incities)

# Modified Dijkstra to find solution
act = s
last = s
while last != d:
    for c in matrix[act]:
        new = cities[act][DISTANCE] + matrix[act][c]
        if (cities[c][DISTANCE] is None) or (cities[c][DISTANCE] > new):
            if cities[c][INCITIESIDX] is None:
                cities[c][LEVEL] = 1
                cities[c][DISTANCE] = new
                cmin.update(cities[c][OUTCITIESIDX])
            elif c != cities[act][BESTNEXT]:
                cities[c][DISTANCE] = new
                dmin.update(cities[c][INCITIESIDX])

    g = cmin.get()
    if g is not None:
        mn = outcities[g]
    if g is None or cities[mn][DISTANCE] is None or cities[mn][LEVEL] == 0:
        nxt = cities[last][BESTNEXT]
        ct = cities[incities[dmin.get()]]
        if ct[DISTANCE] is not None and ct[LEVEL] == 1:
            if last < nxt:
                r = (last, nxt)
            else:
                r = (nxt, last)
            roads[r] = bestdistance + ct[DISTANCE] - ct[BESTDISTANCE]
        act = nxt
        cities[act][LEVEL] = 0
        cities[act][DISTANCE] = cities[act][BESTDISTANCE]
        dmin.update(cities[act][INCITIESIDX])
        last = nxt
        continue
    cities[mn][LEVEL] = 0
    cmin.update(cities[mn][OUTCITIESIDX])
    act = mn

for i in range(q):
    u, v = tuple(map(int, raw_input().split()))
    if v < u:
        u, v = v, u
    print roads[(u, v)]