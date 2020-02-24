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


# :warning: python_library_typed/geometry/geometry.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#8f04bd9e27216e5afe99d60f70335c05">python_library_typed/geometry</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library_typed/geometry/geometry.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 15:17:08+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
eps = 1e-10


def add(a, b):
    return 0 if abs(a + b) < eps * (abs(a) + abs(b)) else a + b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(add(self.x, p.x), add(self.y, p.y))

    def __sub__(self, p):
        return Point(add(self.x, -p.x), add(self.y, -p.y))

    def __mul__(self, d):
        return Point(self.x * d, self.y * d)

    def dot(self, p):
        return add(self.x * p.x, self.y * p.y)

    def det(self, p):
        return add(self.x * p.y, -self.y * p.x)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

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
