from typing import List
import heapq

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:

        INF = 10**18
        n = len(source)

        # ---------- Build Trie ----------
        child = [[-1] * 26]
        tid = [-1]

        def new_node():
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1

        idx = -1

        def add(word: str):
            nonlocal idx
            node = 0
            for ch in word:
                c = ord(ch) - 97
                if child[node][c] == -1:
                    child[node][c] = new_node()
                node = child[node][c]
            if tid[node] == -1:
                idx += 1
                tid[node] = idx
            return tid[node]

        graph = {}
        for i in range(len(original)):
            u = add(original[i])
            v = add(changed[i])
            graph.setdefault(u, []).append((v, cost[i]))

        P = idx + 1
        if P == 0:
            return 0 if source == target else -1

        # ---------- Dijkstra for each node ----------
        dist = [[INF] * P for _ in range(P)]

        for src in range(P):
            pq = [(0, src)]
            dist[src][src] = 0
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[src][u]:
                    continue
                for v, w in graph.get(u, []):
                    nd = d + w
                    if nd < dist[src][v]:
                        dist[src][v] = nd
                        heapq.heappush(pq, (nd, v))

        # ---------- DP ----------
        dp = [INF] * (n + 1)
        dp[0] = 0

        s = [ord(c) - 97 for c in source]
        t = [ord(c) - 97 for c in target]

        for i in range(n):
            if dp[i] == INF:
                continue

            # single character
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            u = v = 0
            for j in range(i, n):
                u = child[u][s[j]]
                v = child[v][t[j]]
                if u == -1 or v == -1:
                    break

                uid = tid[u]
                vid = tid[v]
                if uid != -1 and vid != -1:
                    dp[j + 1] = min(dp[j + 1], dp[i] + dist[uid][vid])

        return -1 if dp[n] == INF else dp[n]
