---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../../assets/css/copy-button.css" />


# :warning: python_library_typed/graph/warshall_floyd.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#2a7e3e97022ce18b59747afed7368880">python_library_typed/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library_typed/graph/warshall_floyd.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 15:17:08+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from typing import List


class Graph_AdjMat:
    def __init__(self, V: int, init: int = 10**9) -> None:
        self.V: int = V
        self.E: List[List[int]] = [[init] * V for _ in range(V)]

    def add_edge(self, src: int, dst: int, weight: int) -> None:
        self.E[src][dst] = weight


class WarshallFloyd():
    def __init__(self, G: Graph_AdjMat, INF: int = 10**9) -> None:
        self.G: Graph_AdjMat = G
        self.INF: int = INF
        self.distance: List[List[int]] = [[self.INF] * G.V for _ in range(G.V)]
        for i in range(G.V):
            self.distance[i][i] = 0
        for fr in range(G.V):
            for to in range(G.V):
                self.distance[fr][to] = G.E[fr][to]

    def run(self) -> None:
        for k in range(self.G.V):
            for i in range(self.G.V):
                for j in range(self.G.V):
                    if self.distance[i][k] != self.INF and \
                       self.distance[k][j] != self.INF:
                        self.distance[i][j] \
                            = min(self.distance[i][j],
                                  self.distance[i][k] + self.distance[k][j])

    def hasNegativeCycle(self) -> bool:
        for i in range(self.G.V):
            if self.distance[i][i] < 0:
                return True
        return False

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 348, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=self.cpp_source_path)
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 68, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>
