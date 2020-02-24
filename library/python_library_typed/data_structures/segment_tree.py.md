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


# :warning: python_library_typed/data_structures/segment_tree.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#1bd6c8bcf0a034068d4ecd4538188ccf">python_library_typed/data_structures</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library_typed/data_structures/segment_tree.py">View this file on GitHub</a>
    - Last commit date: 2020-02-16 02:53:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import math
from typing import Generic, TypeVar, Callable, List

T = TypeVar("T", int, float)



class SegmentTree(Generic[T]):
    """
    Segment Tree
    query:
    1. update(i, val): update i-th value to val
    2. query(low, high): find f(value) in [low, high)
    time complexity: O(log n)
    space complexity: O(2n)
    """
    def __init__(self, N: int, f: Callable[[T, T], T], default: T) -> None:
        self.N = 1 << math.ceil(math.log(N, 2))
        self.default: T = default
        self.f: Callable[[T, T], T] = f
        self.segtree: List[T] = [self.default] * (self.N * 2 - 1)

    def update(self, i: int, val: T) -> None:
        i += self.N - 1
        self.segtree[i] = val
        while i > 0:
            i = (i - 1) // 2
            self.segtree[i] = self.f(self.segtree[2*i+1], self.segtree[2*i+2])

    def query(self, low: int, high: int, k: int = 0, left: int = 0, right: int = -1) -> T:
        if right == -1:
            right = self.N
        if right <= low or high <= left:
            return self.default

        if low <= left and right <= high:
            return self.segtree[k]
        else:
            mid = (left + right) // 2
            return self.f(self.query(low, high, 2*k+1, left, mid),
                          self.query(low, high, 2*k+2, mid, right))

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 348, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=self.cpp_source_path)
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/other.py", line 48, in bundle
    return subprocess.check_output(shlex.split(command))
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/subprocess.py", line 411, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/subprocess.py", line 512, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

