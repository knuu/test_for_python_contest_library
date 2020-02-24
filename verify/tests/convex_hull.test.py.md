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
<script type="text/javascript" src="../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../assets/css/copy-button.css" />


# :heavy_check_mark: tests/convex_hull.test.py

<a href="../../index.html">Back to top page</a>

* <a href="{{ site.github.repository_url }}/blob/master/tests/convex_hull.test.py">View this file on GitHub</a>
    - Last commit date: 2020-02-16 07:49:55+09:00




## Depends on

* :heavy_check_mark: <a href="../../library/python_library/geometry/convex_hull.py.html">python_library/geometry/convex_hull.py</a>
* :heavy_check_mark: <a href="../../library/python_library/geometry/geometry.py.html">python_library/geometry/geometry.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A
# @import python_library/geometry/geometry.py
# @import python_library/geometry/convex_hull.py
import sys

sys.path.insert(0, ".")
input = sys.stdin.buffer.readline

from python_library.geometry.geometry import Point
from python_library.geometry.convex_hull import ConvexHull


def main() -> None:
    N = int(input())
    ps = []
    for _ in range(N):
        x, y = map(int, input().split())
        ps.append(Point(x, y))
    hull = ConvexHull(ps)
    convex = hull.run()
    print(len(convex))
    min_idx = -1
    min_x, min_y = 10001, 10001
    for i, p in enumerate(convex):
        if p.y < min_y or (p.y == min_y and p.x < min_x):
            min_idx = i
            min_x, min_y = p.x, p.y
    for p in convex[min_idx:]:
        print(p.x, p.y)
    for p in convex[:min_idx]:
        print(p.x, p.y)


if __name__ == "__main__":
    main()

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

<a href="../../index.html">Back to top page</a>

