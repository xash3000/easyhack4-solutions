/* Enter your code here. Read input from STDIN. Print output to STDOUT */
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

enum {SIZE = 200000 + 4, INF = 1LL<<61};

typedef long long ll_t;

struct node {
    int who;
    ll_t value;
};

static node heap[SIZE];
static int idx[SIZE];

class binheap {
    int size;

    inline void _swap(int a, int b)
    {
        swap(heap[a], heap[b]);
        idx[heap[a].who] = a;
        idx[heap[b].who] = b;
    }

public:
    binheap(int n) : size(n)
    {
        for (int i = 1; i <= n; i++) {
            idx[i] = i;
            heap[i].who = i;
            heap[i].value = INF;
        }
    }

    inline ll_t getvalue(int who) const
    {
        return heap[idx[who]].value;
    }

    inline ll_t findmin() const
    {
        return heap[1].value;
    }

    inline void decrease(int who, ll_t value)
    {
        int k = idx[who];
        heap[k].value = value;
        while (k > 1 and value < heap[k/2].value) {
            _swap(k, k / 2);
            k /= 2;
        }
    }

    inline void heapify(int k)
    {
        int minidx = k;
        if (2*k <= size and heap[2*k].value < heap[minidx].value)
            minidx = 2*k;
        if (2*k+1 <= size and heap[2*k+1].value < heap[minidx].value)
            minidx = 2*k+1;
        if (minidx != k) {
            _swap(k, minidx);
            heapify(minidx);
        }
    }

    inline void del(int who)
    {
        int k = idx[who];
        _swap(k, size);
        size--;
        heapify(k);
    }

    inline node extractmin()
    {
        node ret = heap[1];
        del(heap[1].who);
        return ret;
    }

    inline bool empty() const
    {
        return size == 0;
    }
};

static vector<pair<int, int> > adj[SIZE];
static vector<int> sub[SIZE];

class graph {
    int size;
public:
    graph(int n) : size(n) {}

    inline void add(int a, int b, int w)
    {
        adj[a].push_back(make_pair(b, w));
    }

    ll_t dijkstra(int s, int t, int *parent, ll_t *length)
    {
        binheap que(size);
        que.decrease(s, 0);
        parent[s] = 0;
        ll_t ret = INF;
        while (!que.empty()) {
            node now = que.extractmin();
            int who = now.who;
            ll_t len = now.value;
            length[who] = len;
            for (vector<pair<int, int> >::iterator vi = adj[who].begin(); vi != adj[who].end(); ++vi) {
                int to = vi->first;
                ll_t w = len + vi->second;
                if (w < que.getvalue(to)) {
                    que.decrease(to, w);
                    parent[to] = who;
                }
            }
            if (who == t)
                ret = len;
        }
        return ret;
    }
};

static char valid[SIZE];
static ll_t slength[SIZE], tlength[SIZE];

static void inline
del(int from, int to, binheap &heap)
{
    if (from == to)
        return;
    heap.del(from);
    valid[from] = 0;
    for (vector<int>::iterator vi = sub[from].begin(); vi != sub[from].end(); ++vi)
        del(*vi, to, heap);
}

static void inline
check(int from, int to, binheap &heap, int root)
{
    if (from == to)
        return;
    for (vector<int>::iterator vi = sub[from].begin(); vi != sub[from].end(); ++vi)
        check(*vi, to, heap, root);
    for (vector<pair<int,int> >::iterator vi = adj[from].begin(); vi != adj[from].end(); ++vi) {
        int v = vi->first;
        if (!valid[v])
            continue;
        if (from == root and v == to)
            continue;
        ll_t w = slength[from] + vi->second + tlength[v];
        if (w < heap.getvalue(v))
            heap.decrease(v, w);
    }
}

int
main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    graph g(n);
    static int sparent[SIZE], tparent[SIZE];
    while (m--) {
        int a, b, w;
        scanf("%d%d%d", &a, &b, &w);
        a++;
        b++;
        g.add(a, b, w);
        g.add(b, a, w);
    }
    int s, t;
    scanf("%d%d", &s, &t);
    s++;
    t++;
    ll_t best = g.dijkstra(s, t, sparent, slength);
    if (best == INF) {
        int q;
        scanf("%d", &q);
        while (q--)
            printf("Infinity\n");
        return 0;
    }

    for (int i = 1; i <= n; i++)
        sub[sparent[i]].push_back(i);
    int i = t, eid = 0;
    map<pair<int, int>, int>path;
    static int nodes[SIZE];
    while (i != s) {
        int p = sparent[i], a = p, b = i;
        if (a > b)
            swap(a, b);
        path.insert(make_pair(make_pair(a, b), eid));
        nodes[eid++] = i;
        i = p;
    }
    g.dijkstra(t, s, tparent, tlength);
    binheap heap(n);
    for (int i = 1; i <= n; i++)
        valid[i] = 1;
    static ll_t replace[SIZE];
    int from = s;
    for (int i = eid - 1; i >= 0; i--) {
        int to = nodes[i];
        del(from, to, heap); 
        check(from, to, heap, from);
        replace[i] = heap.findmin();
        from = to;
    }

    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b;
        scanf("%d%d", &a, &b);
        a++;
        b++;
        if (a > b)
            swap(a, b);
        map<pair<int,int>, int>::iterator mi = path.find(make_pair(a, b));
        if (mi == path.end())
            printf("%lld\n", best);
        else {
            ll_t w = replace[mi->second];
            if (w == INF)
                printf("Infinity\n");
            else
                printf("%lld\n", w);
        }
    }

    return 0;
}
