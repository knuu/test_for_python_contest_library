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


# :warning: python_library_typed/data_structures/fenwick_tree.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#1bd6c8bcf0a034068d4ecd4538188ccf">python_library_typed/data_structures</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library_typed/data_structures/fenwick_tree.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 14:44:54+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import math
from typing import List


class FenwickTree1:
    """
    FenwickTree(Binary Indexed Tree)
    total number: n
    queries:
    1. add(i, val): add val to i-th value
    2. sum(n): sum(bit[1] + ... + bit[n])
    complexity: O(log n)

    Self-balancing binary search tree or Segment Tree can do the same,
    it takes longer to program and complexity also increases.
    Thanks: http://hos.ac/slides/20140319_bit.pdf

    used in ARC031 C, indeednow finalB E
    """
    def __init__(self, a_list: List[int]) -> None:
        # 1-index
        self.N: int = len(a_list)
        self.bit: List[int] = a_list[:]
        for i in range(1, self.N):
            self.bit[i + (i & -i)] += self.bit[i]

    def add(self, idx: int, val: int) -> None:
        while idx <= self.N:
            self.bit[idx] += val
            idx += idx & -idx

    def sum(self, n: int) -> int:
        ret: int = 0
        while n > 0:
            ret += self.bit[n]
            n -= n & -n
        return ret


class FenwickTree:
    def __init__(self, a_list: List[int]) -> None:
        # 0-indexed
        self.N: int = len(a_list)
        self.bit: List[int] = a_list[:]
        for _ in range(self.N, 1 << (math.ceil(math.log(self.N, 2)))):
            self.bit.append(0)
        for i in range(self.N-1):
            self.bit[i | (i+1)] += self.bit[i]

    def add(self, i: int, val: int) -> None:
        while i < self.N:
            self.bit[i] += val
            i |= i + 1

    def sum(self, n: int) -> int:
        ret: int = 0
        while n >= 0:
            ret += self.bit[n]
            n = (n & (n + 1)) - 1
        return ret

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

