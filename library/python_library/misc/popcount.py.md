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


# :warning: python_library/misc/popcount.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#b234f801618f71357e46912cecf08ace">python_library/misc</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/misc/popcount.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 15:17:08+00:00




## Required by

* :heavy_check_mark: <a href="../graph/maximum_independet_set.py.html">python_library/graph/maximum_independet_set.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import sys
import ctypes


def popcount(N):
    if sys.platform.startswith('linux'):
        libc = ctypes.cdll.LoadLibrary('libc.so.6')
        return libc.__sched_cpucount(ctypes.sizeof(ctypes.c_long), (ctypes.c_long * 1)(N))
    elif sys.platform == 'darwin':
        libc = ctypes.cdll.LoadLibrary('libSystem.dylib')
        return libc.__popcountdi2(N)
    else:
        assert(False)

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

